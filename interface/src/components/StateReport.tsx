import {useEffect, useContext } from 'react'
import mqtt from 'precompiled-mqtt'
import './StateReport.css'
import { TOPIC_STATE_REPORT_JSON, TOPIC_REQUEST_STATE_REPORT as TOPIC_STATE_REPORT_REQUEST } from '../util/topics'
import MqttContext from '../util/mqttContext'

export default function StateReport() {
	const { client: c, messages } = useContext(MqttContext);
	const stateReport = messages[TOPIC_STATE_REPORT_JSON];
	const connected = c?.connected;


	useEffect(() => {
		if (!c) {
			return;
		}
		c.subscribe(TOPIC_STATE_REPORT_JSON, (m) => {
			console.log("subsribed to state report", m);
		});
		c.publish(TOPIC_STATE_REPORT_REQUEST, "");
	}, [])

	return (
		<>
		<div style={{ display: 'flex', flexDirection: 'column' }}>
			<h2>StateReport</h2>
			Connection: {String(connected)}
			<br/>
			<textarea id="stateReport" readOnly value={stateReport}></textarea>
			<button onClick={()=>{c?.publish("mega/req/state-report", "")}}>Pub</button>
			<br/>
		</div>
		</>
	)
}
	