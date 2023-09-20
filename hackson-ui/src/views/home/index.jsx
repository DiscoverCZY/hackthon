import React from "react";
import { Link } from 'react-router-dom';
// material-ui
import {
  Typography,
} from '@mui/material';

import Pingpong from 'components/pingpong';
import './style.css'

const Home = () => {
  return (
    <div id="home">
      <div className="home-menu-wrapper">
        <div className="left" />
        <div className="right" />
        <Pingpong />
        <div className="home-menu">
          <Link className="left" to="/workflow">
            Workflow
          </Link>
          <Link className="right" to="/data-visualization">
            Data Visualization
          </Link>
        </div>
      </div>
    </div>
  )
};

export default Home;