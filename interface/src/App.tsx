import StateReport from './components/StateReport'
import './App.css';
import VerticalSlider from './components/VerticalSlider';
import { Typography, AppBar, Button, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid, Toolbar, Container } from '@mui/material';
import { Castle, PrecisionManufacturing } from '@mui/icons-material';
import MqttProvider from './util/MqttProvider';
import ControlGroup from './components/ControlGroup';
import VideoPlayer from './components/VideoPlayer';

function App() {
  return (
    <>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar>
          <PrecisionManufacturing/>
          <Typography variant="h6">
            A Study of Light
          </Typography>
        </Toolbar>
      </AppBar>
      <MqttProvider url='ws://DEPTH:9001'>
        <Grid container
          direction="row"
          spacing={2}
          justifyContent="center"
          alignContent="center"
          padding={2}
        >
          <Grid item xs={12} sm={6}>
            <VideoPlayer url="localhost:8889/top-cam/"/>
          </Grid>
          <Grid item xs={12} sm={6}>
            <VideoPlayer url="localhost:8889/front-cam/"/>
          </Grid>
        </Grid>
        <Container>
          <ControlGroup/>
          <StateReport/>
          <VerticalSlider/>
        </Container>
      </MqttProvider>
    </>
  );
}

export default App;
