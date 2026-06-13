import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import type { TestRun } from '../types';

export const useTestRunsStore = defineStore('testRuns', () => {
  // State
  const runs = ref<TestRun[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  // Getters (Computed properties)
  const totalRuns = computed(() => runs.value.length);
  const failedRuns = computed(() => runs.value.filter(run => run.status === 'failed').length);
  
  // Actions
  function setRuns(newRuns: TestRun[]) {
    runs.value = newRuns;
  }

  // We will add real API fetching here in Milestone 3. 
  // For now, we mock it.
  async function fetchMockRuns() {
    isLoading.value = true;
    error.value = null;
    
    try {
      // Simulating network delay
      await new Promise(resolve => setTimeout(resolve, 800));
      
      setRuns([
        { id: 'tr_1', name: 'Authentication Flow', status: 'passed', duration_ms: 1200, started_at: new Date().toISOString() },
        { id: 'tr_2', name: 'Payment Gateway Integration', status: 'failed', duration_ms: 4500, started_at: new Date().toISOString() },
        { id: 'tr_3', name: 'User Profile Sync', status: 'running', duration_ms: null, started_at: new Date().toISOString() },
      ]);
    } catch (e) {
      error.value = 'Failed to fetch test runs';
    } finally {
      isLoading.value = false;
    }
  }

  return {
    runs,
    isLoading,
    error,
    totalRuns,
    failedRuns,
    fetchMockRuns,
  };
});