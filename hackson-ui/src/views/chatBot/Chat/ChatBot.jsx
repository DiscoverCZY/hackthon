import React from 'react';
// material-ui
import {
  Avatar,
  CircularProgress,
} from '@mui/material';
import Logo from "components/Logo";
import Chart from 'components/Chart';
import Intro from './IntroSection';
import Error from "./Error";
import Table from "./Table";

const Content = (props) => {
  const { index, message, model, ...config } = props;

  const getComp = (m) => {
    switch (m) {
      case 'chart':
        return Chart;
      case 'table':
        return Table;
      case 'intro':
        return Intro
      case 'string':
      default:
        return null;
    }
  }
  const Comp = getComp(model);
  return (
    <div className='content'>
      {message}
      {Comp && <Comp id={`chat-${index}`} {...config} />}
    </div>
  );
}

const ChatBot = (props) => {
  const { index, actions, chat: { data, role, status } } = props;

  return (
    <section className={`message ${role}`}>
      {
        role === 'ai' &&
        <Avatar bg="#11a27f" className="avatar">
          <Logo w={36} h={36} />
        </Avatar>
      }
      <div className="messageContent">
        {
          status === 'loading' && <div className='loading'><CircularProgress /></div>
        }
        {
          status === 'error' && <Error err={data} />
        }
        {
          status === 'success' && data && (
            <Content {...data} index={index} actions={actions} />
          )
        }
      </div>
    </section>
  );
}

export default ChatBot;