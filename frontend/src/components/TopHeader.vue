<script setup lang="ts">
// Later, this will receive user info or breadcrumbs via props
</script>

<template>
  <header class="top-header">
    <div class="header-title">
      <h2>Agentic Test Dashboard</h2>
    </div>
    <div class="user-profile">
      <span>Admin User</span>
    </div>
  </header>
</template>

<style scoped>
.top-header {
  height: 60px;
  background-color: #ffffff;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
}
.header-title h2 {
  margin: 0;
  font-size: 1.25rem;
  color: #111827;
}
.user-profile {
  font-weight: 500;
  color: #4b5563;
}
</style>