import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: 'jsdom', // Simulates a browser environment
    globals: true,        // Allows us to use describe/it/expect without importing them everywhere
  },
});