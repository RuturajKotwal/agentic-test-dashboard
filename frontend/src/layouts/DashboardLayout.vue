<script setup lang="ts">
import Sidebar from '../components/Sidebar.vue';
import TopHeader from '../components/TopHeader.vue';
</script>

<template>
  <div class="layout-wrapper">
    <Sidebar />
    <div class="main-column">
      <TopHeader />
      <main class="content-area">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style scoped>
.layout-wrapper {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
.main-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0; /* Prevents flexbox overflow bugs */
}
.content-area {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}
</style>