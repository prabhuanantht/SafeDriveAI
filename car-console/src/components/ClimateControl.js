import React, { useState } from "react";

const ClimateControl = () => {
    const [temperature, setTemperature] = useState(22);

    return (
        <div className="climate-control">
            
            <h2>Climate Control</h2>
            <div className="radial-slider-container">
                <input
                    type="range"
                    min="16"
                    max="30"
                    value={temperature}
                    onChange={(e) => setTemperature(e.target.value)}
                    className="radial-slider"
                />
                <div className="radial-slider-overlay">
                    <span>{temperature}°C</span>
                </div>
            </div>
        </div>
    );
};

export default ClimateControl;
