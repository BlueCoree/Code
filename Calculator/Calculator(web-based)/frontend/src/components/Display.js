import React from "react";

const Displayy = ({ expression, result }) => {
    console.log("Display Props:", { expression, result }); 
    const displayValue = result ? `${result}` : expression;

    return (
        <div className="displayy">
            <div className="expression">{expression}</div>
        </div>
    );
};

export default Displayy;
