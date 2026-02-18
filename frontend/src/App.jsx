import React, { useEffect, useState, useRef } from "react";
import LiveStatus from "./components/LiveStatus"; 
import LoopView from "./views/LoopView";
// ... import other views

export default function App() {
  const [personCount, setPersonCount] = useState(0); // State for the Live Header
  const [adsPlaying, setAdsPlaying] = useState(false);
  const [cameraCapturing, setCameraCapturing] = useState(false); // Camera capture status
  const [isConnected, setIsConnected] = useState(false);
  const ws = useRef(null);

  useEffect(() => {
    // Connect to the Python Backend
    const WS_URL = "ws://localhost:8000/ws";
    
    const connectWS = () => {
      ws.current = new WebSocket(WS_URL);

      ws.current.onopen = () => {
        console.log("✅ Connected to Vision System");
        setIsConnected(true);
      };

      ws.current.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          
          // HANDLE FACE DETECTION UPDATE
          if (data.action === "PERSON_DETECTED") {
            setPersonCount(data.count);
            // Camera is capturing when detecting people during ads
            setCameraCapturing(adsPlaying && data.count > 0);
          }
          
          // ... handle other actions (MODE_SWITCH, etc.)
        } catch (err) {
          console.error("Data Error:", err);
        }
      };

      ws.current.onclose = () => {
        setIsConnected(false);
        setTimeout(connectWS, 3000); // Try to reconnect every 3s
      };
    };

    connectWS();
    return () => ws.current?.close();
  }, []);

  return (
    <div className="relative w-screen h-screen bg-black overflow-hidden font-sans">
      
      {/* --- LIVE HEADER (Always on top) --- */}
      <LiveStatus 
        isConnected={isConnected} 
        personCount={personCount} 
        adsPlaying={adsPlaying}
        cameraCapturing={cameraCapturing}
      />

      {/* --- MAIN VIEWS --- */}
      <div className="absolute inset-0 z-0">
         <LoopView systemState={{}} onPlaybackChange={setAdsPlaying} /> 
         {/* You will add your logic here to switch views later */}
      </div>

    </div>
  );
}