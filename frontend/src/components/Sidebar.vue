<script setup lang="ts">
// We use router-link for client-side navigation without page reloads
</script>

<template>
  <aside class="sidebar">
    <div class="logo">
      <h3>AI-QA</h3>
    </div>
    <nav class="nav-links">
      <router-link to="/" class="nav-item">Dashboard</router-link>
      <router-link to="/runs" class="nav-item">Test Runs</router-link>
      <router-link to="/settings" class="nav-item">Settings</router-link>
    </nav>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #1f2937;
  color: #ffffff;
  display: flex;
  flex-direction: column;
}
.logo {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 24px;
  background-color: #111827;
}
.logo h3 {
  margin: 0;
  color: #60a5fa;
}
.nav-links {
  display: flex;
  flex-direction: column;
  padding: 16px 0;
}
.nav-item {
  padding: 12px 24px;
  color: #d1d5db;
  text-decoration: none;
  font-weight: 500;
  transition: background-color 0.2s;
}
.nav-item:hover, .router-link-exact-active {
  background-color: #374151;
  color: #ffffff;
}
</style>