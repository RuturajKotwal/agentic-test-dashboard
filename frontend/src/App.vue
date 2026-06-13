<script setup lang="ts">
// The root component simply provides the router outlet
</script>

<template>
  <router-view />
</template>

<style>
/* Reset basic margins and enforce full screen */
html, body {
  margin: 0;
  padding: 0;
  height: 100vh;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background-color: #f3f4f6; /* Light gray background for contrast */
}
#app {
  height: 100%;
}
</style>