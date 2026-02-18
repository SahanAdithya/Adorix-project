import React from 'react';

export default function LiveStatus({ isConnected, personCount, adsPlaying = false, cameraCapturing = false }) {
  // Determine status color based on connection and detection
  const statusColor = isConnected ? "bg-green-500" : "bg-red-500";
  const glowEffect = isConnected ? "shadow-[0_0_15px_rgba(34,197,94,0.6)]" : "";

  return (
    <div className="absolute top-8 right-8 z-50 flex flex-col items-end gap-2">

      {/* TOP-RIGHT AD PLAYBACK DOT (fixed to screen) */}
      {adsPlaying && (
        <div className="fixed top-3 right-3 z-60">
          <div className="relative h-4 w-4">
            <span className="animate-pulse absolute inline-flex h-full w-full rounded-full bg-green-300 opacity-80"></span>
            <span className="relative inline-flex rounded-full h-4 w-4 bg-green-400 border border-white/30"></span>
          </div>
        </div>
      )}

      {/* CAMERA RECORDING INDICATOR (Center bottom when capturing) */}
      {cameraCapturing && (
        <div className="fixed bottom-1/2 left-1/2 transform -translate-x-1/2 translate-y-1/2 z-60">
          <div className="flex items-center gap-3 px-8 py-4 rounded-lg bg-red-600/90 backdrop-blur-md border-2 border-red-400 shadow-lg shadow-red-600/50 animate-pulse">
            {/* Red recording dot */}
            <div className="flex items-center gap-2">
              <span className="inline-flex h-3 w-3 rounded-full bg-red-300 animate-pulse"></span>
              <span className="text-white font-bold text-lg tracking-widest uppercase">
                CAMERA RECORDING
              </span>
            </div>
          </div>
        </div>
      )}
      
      {/* 1. MAIN SYSTEM STATUS BADGE */}
      <div className={`flex items-center gap-3 px-5 py-2 rounded-full border border-white/10 bg-black/40 backdrop-blur-md transition-all duration-500 ${glowEffect}`}>
        
        {/* Pulsing Indicator Dot */}
        <div className="relative flex h-3 w-3">
          {isConnected && (
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
          )}
          <span className={`relative inline-flex rounded-full h-3 w-3 ${statusColor}`}></span>
        </div>

        <span className="text-white font-mono text-xs font-bold tracking-widest uppercase">
          {isConnected ? "SYSTEM ONLINE" : "DISCONNECTED"}
        </span>
      </div>

      {/* 2. PERSON DETECTION BADGE (Only appears when people are seen) */}
      <div className={`
        flex items-center gap-2 px-4 py-2 rounded-lg border border-green-500/30 bg-green-900/20 backdrop-blur-md
        transition-all duration-500 transform origin-top-right
        ${personCount > 0 ? "opacity-100 scale-100 translate-y-0" : "opacity-0 scale-90 -translate-y-2 pointer-events-none"}
      `}>
        {/* Icon */}
        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0z" />
        </svg>

        <span className="text-green-100 font-mono text-sm font-bold">
          {personCount} {personCount === 1 ? "PERSON" : "PEOPLE"} DETECTED
        </span>
      </div>

    </div>
  );
}