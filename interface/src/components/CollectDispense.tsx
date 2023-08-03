import { useState, useContext, useEffect } from "react";
import { TOPIC_DISPENSE, TOPIC_COLLECT } from "../topics_firmware/topics_firmware";
import { StateReport, Status } from "../machinepb/machine";
import MqttContext from "../util/mqttContext";
import { ButtonGroup, Button, Typography, Slider, Box, Tabs, Tab } from "@mui/material";
import {
  useSessionStatus,
  useStateReport,
  useStreamStatus,
  useSystemVialProfiles,
  useVialProfiles,
} from "../util/hooks";
import { TOPIC_MARK_DELAYED_DISPENSE, TOPIC_MARK_FAILED_DISPENSE } from "../topics_backend/topics_backend";
import { vialDisabled } from "./helpers";
import { useError } from "./ErrorManager";

export default function CollectDispense() {
  const noVials = 6;
  const vials = new Array(noVials - 1).fill(0).map((_, i) => noVials - i);

  const error = useError();
  const { client: c, messages } = useContext(MqttContext);
  const stateReport: StateReport | null = useStateReport();
  const [vialProfiles, setVialProfiles] = useVialProfiles();
  const [systemVialProfiles, setSystemVialProfiles] = useSystemVialProfiles();

  const [dropNumber, setDropNumber] = useState(3);

  const isAwake: boolean =
    !!stateReport && stateReport?.status !== Status.SLEEPING && stateReport?.status !== Status.E_STOP_ACTIVE;

  const collecting: boolean = !!stateReport && stateReport?.collectionRequest?.completed === false;
  const collectingVial = collecting && stateReport?.collectionRequest?.vialNumber;

  // DROP VOLUMES
  // water = 20ul
  // temporary emulsifier = 12ul
  // dye (green) = 14ul
  const dispenseVolumeFromVial = (vial: number | undefined): number => {
    if (!vial) {
      return NaN;
    }

    const vialProfileId = systemVialProfiles?.vials[vial];
    if (vialProfileId === undefined) {
      error(`cannot find system profile for vial ${vial}: ${systemVialProfiles}`);
      return 0;
    }

    const vialProfile = vialProfiles?.profiles[vialProfileId];
    if (vialProfile === undefined) {
      error(`cannot find profile for profileId ${vialProfileId}: ${vialProfiles}`);
      return 0;
    }

    return vialProfile.dispenseVolumeUl;
  };

  const getAutoDispenseVolume = () => {
    return dispenseVolumeFromVial(stateReport?.pipetteState?.vialHeld);
  };

  const requestCollection = (vial: number): void => {
    const volume = dropNumber * dispenseVolumeFromVial(vial);
    if (volume === 0) {
      error("could not get volume");
      return;
    }
    c?.publish(TOPIC_COLLECT, `${vial.toString()},${volume}`);
  };

  const keyDownHandler = (event: KeyboardEvent) => {
    console.log(`key handler, ${dropNumber}, ${event}`);
    const key = event.key;

    const num = parseInt(key, 10);
    if (num >= 1 && num <= noVials) {
      requestCollection(num);
      return;
    }

    switch (key) {
      case " ":
        c?.publish(TOPIC_DISPENSE, getAutoDispenseVolume().toString());
        break;
    }
  };

  const getDispensesRemaining = () => {
    return (stateReport?.pipetteState?.volumeTargetUl ?? 0) / getAutoDispenseVolume();
  };

  useEffect(() => {
    window.addEventListener("keydown", keyDownHandler);
    return () => {
      window.removeEventListener("keydown", keyDownHandler);
    };
  }, [c, stateReport, dropNumber, vialProfiles, systemVialProfiles]);

  // Keeps track of dispense status so the failed / delayed buttons can be greyed
  // out according to what's already been pressed.
  const [latestFailedDispense, setLatestFailedDispense] = useState(-1);
  const markFailedDispense = () => {
    setLatestFailedDispense(stateReport?.pipetteState?.dispenseRequestNumber ?? -1);
    setLatestDelayedDispense(-1);
    c?.publish(TOPIC_MARK_FAILED_DISPENSE, "");
  };
  const [latestDelayedDispense, setLatestDelayedDispense] = useState(-1);
  const markDelayedDispense = () => {
    setLatestDelayedDispense(stateReport?.pipetteState?.dispenseRequestNumber ?? -1);
    setLatestFailedDispense(-1);
    c?.publish(TOPIC_MARK_DELAYED_DISPENSE, "");
  };

  return (
    <>
      <Typography variant="h6">Collection & Dispense</Typography>
      <Slider
        value={dropNumber}
        onChange={(e, value) => (typeof value === "number" ? setDropNumber(value) : null)}
        min={1}
        max={10} // Adjust the max value according to your requirements
        step={1}
        marks={true}
        valueLabelDisplay="auto"
        valueLabelFormat={(value) => `${value}`}
        aria-label="Collection drops"
        sx={{ margin: 2, width: "50%" }}
      />
      <ButtonGroup variant="outlined" aria-label="outlined button group" sx={{ margin: 2 }}>
        {vials.map((vial) => (
          <Button
            key={vial}
            disabled={!isAwake || collecting || vialDisabled(vial)}
            variant={collectingVial === vial ? "contained" : "outlined"}
            onClick={() => requestCollection(vial)}
          >
            {vial}
          </Button>
        ))}
      </ButtonGroup>
      <Typography variant="body1">Dispenses remaining: {getDispensesRemaining()}</Typography>
      <Typography variant="body1">Auto-Dispense Volume: {getAutoDispenseVolume()}µl</Typography>
      <Button
        disabled={!isAwake || collecting || stateReport?.pipetteState?.spent}
        onClick={() => c?.publish(TOPIC_DISPENSE, getAutoDispenseVolume().toString())}
        sx={{ margin: 1 }}
      >
        Auto-Dispense
      </Button>
      <Button
        color="error"
        disabled={
          !isAwake ||
          stateReport?.pipetteState?.dispenseRequestNumber === latestFailedDispense ||
          stateReport?.pipetteState?.dispenseRequestNumber === 0
        }
        onClick={markFailedDispense}
      >
        Mark Failed Dispense
      </Button>
      <Button
        color="error"
        disabled={
          !isAwake ||
          stateReport?.pipetteState?.dispenseRequestNumber === latestDelayedDispense ||
          stateReport?.pipetteState?.dispenseRequestNumber === 0
        }
        onClick={markDelayedDispense}
      >
        Mark Delayed Dispense
      </Button>
    </>
  );
}
