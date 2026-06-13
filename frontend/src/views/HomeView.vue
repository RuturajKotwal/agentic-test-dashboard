<script setup lang="ts">
  import { useTestRunsStore } from '../store/testRuns'
  const store = useTestRunsStore()
</script>

<template>
  <div>
    <h1>System Overview</h1>
    <p>Welcome to the Agentic Test Dashboard. This is the main content area.</p>
    <p>Total Runs: {{ store.totalRuns }}</p>
    <p>Failed Runs: {{ store.failedRuns }}</p>
  </div>
</template>