import React, { useState } from "react";
import Navigation from "./components/Navigation";
import SeatSettings from "./components/SeatSettings";
import MusicPlaylist from "./components/MusicPlaylist";
import ClimateControl from "./components/ClimateControl";
import Odometer from "./components/Odometer";

import "./App.css";

const App = () => {
    const [activeTab, setActiveTab] = useState("seat");

    return (
        <div className="app">
          
            <div className="background"></div>
            
            <div className="dashboard-container">
                <Navigation setActiveTab={setActiveTab} activeTab={activeTab} />
                
                <div className={`content content-${activeTab}`}>
                    {activeTab === "seat" && <SeatSettings />}
                    {activeTab === "music" && <MusicPlaylist />}
                    {activeTab === "climate" && <ClimateControl />}
                    {activeTab === "odometer" && <Odometer />}
                </div>
                
            </div>
            
        </div>
        
    );
};

export default App;
