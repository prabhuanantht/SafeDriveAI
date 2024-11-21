import React, { useState } from "react";

const MusicPlaylist = () => {
    const [songs, setSongs] = useState([]);
    const [newSong, setNewSong] = useState("");

    const addSong = () => {
        if (newSong.trim()) {
            setSongs([...songs, newSong.trim()]);
            setNewSong("");
        }
    };

    const removeSong = (index) => {
        setSongs(songs.filter((_, i) => i !== index));
    };

    return (
        <div className="music-playlist">
            
            <h2>Music Playlist</h2>
            <ul className="playlist-list">
                {songs.map((song, index) => (
                    <li key={index} className="playlist-item">
                        {song}
                        <button className="remove-btn" onClick={() => removeSong(index)}>
                            ✖
                        </button>
                    </li>
                ))}
            </ul>
            <div className="add-song-container">
                <input
                    type="text"
                    placeholder="Add new song"
                    value={newSong}
                    onChange={(e) => setNewSong(e.target.value)}
                    className="song-input"
                />
                <button onClick={addSong} className="add-song-btn">
                    Add Song
                </button>
            </div>
        </div>
    );
};

export default MusicPlaylist;
