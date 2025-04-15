import react from "react";
import "./Button.css";

const Button = ({ label, onClick }) => {
    const isOperator = /[+\-*/=C←]/.test(label);
    const isEmpty = false;
    const isZero = label === "0";
    const isBackspace = label === "←";
    const isSpacebar = label === "␣";

    let className = "button";
    if (isOperator) className += " operator";
    if (isZero) className += " zero";
    if (isBackspace) className += " backspace";
    if (isSpacebar) className += " spacebar";

    const displayLabel = isSpacebar ? "␣" :label;

    return(
        <button 
        className={className} 
        onClick={() => onClick(label)}>
            {displayLabel}
        </button>
    );
};

export default Button;
