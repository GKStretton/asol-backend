import React, { useState, useContext } from 'react';
import MqttContext from '../util/mqttContext'
import { TOPIC_GOTO_XY } from '../util/topics';
import VideoPlayer from './VideoPlayer';

const TopCamPlayer = () => {
  const [circlePos, setCirclePos] = useState<{ x: number; y: number }>({ x: 0, y: 0 });
	const { client: c, messages } = useContext(MqttContext);

  const handleClick = (e: React.MouseEvent<HTMLVideoElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const normalizedX = (x / rect.width) * 2 - 1;
    const normalizedY = -((y / rect.height) * 2 - 1);

    console.log(`Clicked at normalized coordinates: (${normalizedX}, ${normalizedY})`);

    setCirclePos({ x: normalizedX, y: normalizedY });

    c?.publish(TOPIC_GOTO_XY, `${normalizedX},${normalizedY}`)
  };

  const renderOverlay = (videoDimensions: { width: number; height: number }) => (
    <div
      style={{
        position: 'absolute',
        border: '5px solid red',
        borderRadius: '50%',
        width: '20px',
        height: '20px',
        left: `${(circlePos.x + 1) * 0.5 * videoDimensions.width}px`,
        top: `${(-circlePos.y + 1) * 0.5 * videoDimensions.height}px`,
        transform: 'translate(-50%, -50%)',
      }}
    ></div>
  );

  return (
    <VideoPlayer
	  url="DEPTH:8889/top-cam-crop/"
      name="top"
      handleClick={handleClick}
      renderOverlay={renderOverlay}
    />
  );
};

export default TopCamPlayer;
