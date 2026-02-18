import React, { useState } from "react";

// ✅ UPDATED: Exact file names from your screenshot
const AD_PLAYLIST = [
  "/ads/10-15_female.mp4",
  "/ads/10-15_male.mp4",
  "/ads/16-29_female.mp4",
  "/ads/16-29_male.mp4",
  "/ads/30-39_female.mp4",
  "/ads/30-39_male.mp4",
  "/ads/40-49_female.mp4",
  "/ads/40-49_male.mp4",
  "/ads/50-59_female.mp4",
  "/ads/50-59_male.mp4",
  "/ads/above-60_female.mp4",
  "/ads/above-60_male.mp4"
];

export default function LoopView({ systemState, onPlaybackChange }) {
  const [currentVideoIndex, setCurrentVideoIndex] = useState(0);

  // Function to switch to the next video when one finishes
  const handleVideoEnd = () => {
    setCurrentVideoIndex((prevIndex) => {
      // If we reach the end of the list, go back to 0 (Loop)
      return (prevIndex + 1) % AD_PLAYLIST.length;
    });
  };

  return (
    <video
      key={AD_PLAYLIST[currentVideoIndex]}
      src={AD_PLAYLIST[currentVideoIndex]}
      autoPlay
      muted
      playsInline
      className="fixed inset-0 w-screen h-screen object-cover"
      onPlay={() => onPlaybackChange?.(true)}
      onPause={() => onPlaybackChange?.(false)}
      onEnded={handleVideoEnd}
      onError={(e) => {
        console.error("Missing video:", AD_PLAYLIST[currentVideoIndex]);
        handleVideoEnd();
      }}
    />
  );
}