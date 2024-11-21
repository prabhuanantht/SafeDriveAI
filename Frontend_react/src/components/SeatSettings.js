import React, { useState } from "react";

const SeatSettings = () => {
    const [height, setHeight] = useState(10);
    const [recline, setRecline] = useState(5);

    return (
        <div className="seat-settings">
            
            <h2>Seat Settings</h2>
            <div className="slider-container">
                <div className="slider-wrapper">
                    <label>Height</label>
                    <input
                        type="range"
                        className="vertical-slider"
                        min="0"
                        max="20"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                    />
                    <span className="slider-value">{height}</span>
                </div>
                <div className="slider-wrapper">
                    <label>Recline</label>
                    <input
                        type="range"
                        className="vertical-slider"
                        min="0"
                        max="15"
                        value={recline}
                        onChange={(e) => setRecline(e.target.value)}
                    />
                    <span className="slider-value">{recline}</span>
                </div>
            </div>
        </div>
    );
};

export default SeatSettings;
