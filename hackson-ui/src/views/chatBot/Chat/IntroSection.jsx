import React from "react";
import { Typography, Link } from "@mui/material";
// import Upload from './Upload';


const IntroSection = ({ actions }) => {
  const onQuestionClick=(e)=>{
    actions.onSystemSend(e.target.innerText);
  };

  return (
    <div id="introsection">
      <Typography variant="h4" component="h4" gutterBottom>
        Introducing Talkbot
      </Typography>
      <Typography variant="h6" component="h6" gutterBottom>
        Converts Text to SQL and return query results
      </Typography>
      {/* <Upload onUpload={actions.onUpload}>Upload a file</Upload> */}
      <div className="question">
        <Link component="button" className="link" onClick={onQuestionClick}>question1</Link>
        <Link component="button" className="link" onClick={onQuestionClick}>question2</Link>
        <Link component="button" className="link" onClick={onQuestionClick}>question3</Link>
        <Link component="button" className="link" onClick={onQuestionClick}>question4</Link>
      </div>
    </div>
  );
};

export default IntroSection;