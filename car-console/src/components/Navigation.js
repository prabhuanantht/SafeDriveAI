import React from "react";

const Navigation = ({ setActiveTab }) => {
    const tabs = [
        { id: "seat", label: "Seat Settings" },
        { id: "music", label: "Music Playlist" },
        { id: "climate", label: "Climate Control" },
        { id: "odometer", label: "Odometer" },
    ];

    return (
        <div className="navigation">
            <h1>Hi Ananth!</h1>
            {tabs.map((tab) => (
                <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className="nav-button"
                >
                    {tab.label}
                </button>
                
            ))}
        </div>
        
    );
};

export default Navigation;
