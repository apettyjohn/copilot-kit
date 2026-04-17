import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  serverExternalPackages: ["pino", "thread-stream"],
  allowedDevOrigins: [
    '100.105.199.27',  // Your Tailscale/client IP
    '163.245.210.68',  // VPS IP
    'localhost',
    '127.0.0.1'
  ],
};

export default nextConfig;