import React, { useState } from "react";
import axios from "axios";
import Displayy from "./Display";
import Button from "./Button";
import "./App.css";

const App = () => {
    const [expression, setExpression] = useState("");
    const [result, setResult] = useState("");

    const handleClick = (value) => {
        if (value === "=") {
            console.log("Sending expression to backend:", expression);
            axios
              .post("http://localhost:5000/calculate", { expression })
              .then((res) => {
                console.log("Response from backend:", res.data);
                setResult(res.data.result); 
                setExpression(res.data.result.toString()); 
              })
              .catch((err) => {
                console.error("Error from backend:", err);
                setResult("Error");
              });
        } else if (value === "C") {
            setExpression(""); 
            setResult(""); 
        } else if (value === "←") {
            setExpression(expression.slice(0, -1)); 
        } else if (value === "␣") {
            setExpression(expression + " "); 
        } else if (["+", "-", "*", "/"].includes(value)) {
            if (expression && !/[\+\-\*/]$/.test(expression)) {
                setExpression(expression + value); 
            }
        } else {
            setExpression(expression + value); 
        }
    };

    const buttons = [
      "7", "8", "9", "/",
      "4", "5", "6", "*",
      "1", "2", "3", "-",
      "0", ".", "C", "+",
      "←", "␣", "="
    ];

    return (
        <div className="calculator">
            <Displayy expression={expression} result={result} />
            <div className="buttons">
              {buttons.map((btn, i) => (
                <Button 
                  key={i} 
                  label={btn} 
                  onClick={() => handleClick(btn)}
                />
              ))}
            </div>
        </div>
    );
};

export default App;