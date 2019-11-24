import React, { useState } from 'react';
import Dialog from '@material-ui/core/Dialog';
import Button from '@material-ui/core/Button';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { setSyntheticLeadingComments } from 'typescript';


function Alert({show, title, message, handleClose}) {

  // if (show === true) {
  //   setOpen(true);
  // }

  // const error = (title, message) => {
  //   setOpen(true);
  //   title = title;
  //   message = message;
  // };

  // if (show === true) {
    return (
      <Dialog
      open={show}
      onClose={handleClose}
      aria-labelledby="alert-dialog-title"
      aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{title}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {message}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Okay
          </Button>
        </DialogActions>
      </Dialog>
    )
  // } else {
  //   return (
  //     <div></div>
  //   )
  // }
  
 }

export default (Alert);