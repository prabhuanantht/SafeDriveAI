import React from "react";

const Odometer = () => {
    return (
        <div className="odometer">
            
            <h2>Odometer</h2>
            <div className="odometer-circle">
                <span className="odometer-speed">60</span>
                <span className="odometer-label">km/h</span>
            </div>
            <p>Total Distance: 12,345 km</p>
        </div>
    );
};

export default Odometer;
