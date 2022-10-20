import React from "react";
// import ReactDOM from "react-dom/client";
import classes from "./Model.module.css";

const BackDrop = (props) => {
  return <div className={classes.backdrop} onClick={props.onClose} />;
};

const ModalOverlay = (props) => {
  return (
    <div className={classes.modal}>
      <div className={classes.content}> {props.children} </div>
    </div>
  );
};

// const portalElement = document.getElementById("overlays");

const Model = (props) => {
  return (
    <>
      {/* {ReactDOM.createPortal(<BackDrop />, portalElement)}
                  {ReactDOM.createPortal(
                    <ModalOverlay> {props.children} </ModalOverlay>,
                    portalElement
                  )} */}
      <BackDrop onClose={props.onClose} />
      <ModalOverlay> {[props.children]} </ModalOverlay>
    </>
  );
};

export default Model;
