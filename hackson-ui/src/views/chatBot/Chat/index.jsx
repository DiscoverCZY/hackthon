import React, { useEffect, useRef, useState } from "react";
import { Box, Menu, IconButton, MenuItem } from "@mui/material";
import { Send, Delete as DeleteIcon, MoreVert } from '@mui/icons-material';
import * as ChatModel from 'mock/ChatModel';
import ChatBot from "./ChatBot";

import "./style.css";

const API_KEY = "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";

const defaultChatLog = {
  status: 'success',
  role: 'ai',
  data: ChatModel.intro
}

const Chat = ({ userid }) => {
  const [inputPrompt, setInputPrompt] = useState("");
  const [chatLog, setChatLog] = useState([defaultChatLog]);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({
        behavior: "smooth",
        block: "end",
      });
    }
    if (chatLog.length > 1) localStorage.setItem("chatLog", JSON.stringify(chatLog));
  }, [chatLog]);

  const setFetchData = (status, data, index) => {
    setChatLog(prevState => {
      if (!prevState.length) return prevState;
      prevState[index] = {
        ...prevState[index],
        status,
        data: data
      }
      return [...prevState];
    });
  }

  const onCallBot = async (message, index) => {
    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: {
          "Authorization": "Bearer " + API_KEY,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message,
          userid,
        }),
      });
      const _data = await response.json();
      const tableData = {
        ...ChatModel.table,
        ..._data
      }
      setFetchData('success', tableData, index);
    } catch (err) {
      // setFetchData('error', err, index);
      setFetchData('success', ChatModel.table, index);
    }
  }
  const onSystemSend = async (message, fn) => {
    setChatLog(prevState => (
      [...prevState,
      {
        role: 'sys',
        status: 'success',
        data: { message }
      },
      {
        role: 'ai',
        status: 'loading',
        data: { message }
      },
      ]
    ));

    const msgIndex = chatLog.length + 1;

    if (fn) {
      fn(msgIndex)
    } else {
      onCallBot(message, msgIndex);
    }

  }

  const onUpload = (file) => {
    const handleUpload = (index) => {
      const formdata = new FormData();
      formdata.append('file', file);

      fetch('http://localhost:4000/api/upload', {
        method: 'POST',
        body: formdata,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(async (response) => {
        // const _data = await response.json();
        setFetchData('success', { message: 'File upload success' }, index);
      }
      ).catch(error => {
        console.error(error);
        setFetchData('error', { message: 'Failed to upload' }, index);
      });
    };
    const message = `Upload File: ${file.name}`;
    onSystemSend(message, handleUpload)
  }

  const clearHistory = () => {
    setChatLog([defaultChatLog]);
    localStorage.removeItem("chatLog");
  };

  useEffect(() => {
    const getHistory = () => {
      const _chatLog = JSON.parse(localStorage.getItem('chatLog')) || [defaultChatLog];
      if (_chatLog) {
        setChatLog(_chatLog);
        _chatLog.forEach((log, index) => {
          if (log.status === 'loading') {
            onCallBot(log.data.message, index);
          }
        });
      };
    };
    if (userid) getHistory();
    return () => {
      localStorage.setItem("chatLog", JSON.stringify(chatLog));
    }
  }, [userid]);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (inputPrompt.trim() !== "") {
      onSystemSend(inputPrompt);
    }

    setInputPrompt("");
  };

  const [anchorEl, setAnchorEl] = useState();
  const onMoreClick = (e) => {
    if (!e) setAnchorEl();
    else setAnchorEl(e.currentTarget);
  }

  const actions = { onUpload, onSystemSend }

  return (
    <Box className="chat">
      <Box sx={{ boxShadow: 1, height: '100%' }} className="chatBox">
        <div id="chatLog" className="chatLog">
          {
            chatLog.map((chat, idx) => {
              return (
                <ChatBot
                  key={idx}
                  index={idx}
                  chat={chat}
                  actions={actions}
                />
              );
            })
          }
          <div className="end" ref={chatEndRef} />
        </div>
        <form onSubmit={handleSubmit} className="promptFrom">
          <div className="inputPromptWrapper">
            <input
              name="inputPrompt"
              id=""
              className="inputPrompttTextarea"
              type="text"
              rows="1"
              value={inputPrompt}
              onChange={(e) => setInputPrompt(e.target.value)}
              autoFocus
              placeholder="Type message here"
            ></input>
            <IconButton color="secondary" aria-label="form submit" type="submit" title="submit">
              <Send />
            </IconButton>
            <IconButton
              aria-label="more"
              id="more-button"
              aria-controls={!!anchorEl ? 'long-menu' : undefined}
              aria-expanded={!!anchorEl ? 'true' : undefined}
              aria-haspopup="true"
              onClick={onMoreClick}
            >
              <MoreVert />
            </IconButton>
          </div>
        </form>
      </Box>
      <Menu
        id="more-menu"
        MenuListProps={{
          'aria-labelledby': 'more-button',
        }}
        anchorEl={anchorEl}
        open={!!anchorEl}
        onClose={() => onMoreClick(false)}
      >
        <MenuItem key="delete" onClick={clearHistory}>
          <DeleteIcon /> Clear chat history
        </MenuItem>
      </Menu>
      {/* <Box className="toolbar">
        <ButtonGroup className="actions">
          <Upload aria-label="upload" title="Upload a file" onUpload={onUpload} />
          <IconButton
            aria-label="delete"
            title="Clear chat history"
            onClick={clearHistory}
            disabled={!chatLog.length}
          >
            <DeleteIcon />
          </IconButton>
        </ButtonGroup>
      </Box> */}
    </Box>
  );
};

export default Chat;
