import { setActivePinia, createPinia } from 'pinia';
import { useTestRunsStore } from './testRuns';
import { describe, it, expect, beforeEach } from 'vitest';

describe('TestRuns Store', () => {
  // A fresh Pinia instance is created before EACH test to prevent state leakage
  beforeEach(() => {
    setActivePinia(createPinia());
  });

  it('initializes with an empty state', () => {
    const store = useTestRunsStore();
    expect(store.runs).toEqual([]);
    expect(store.isLoading).toBe(false);
    expect(store.error).toBeNull();
    expect(store.totalRuns).toBe(0);
    expect(store.failedRuns).toBe(0);
  });

  it('calculates total and failed runs correctly', () => {
    const store = useTestRunsStore();
    
    // Manually setting state to test the getters
    store.runs = [
      { id: '1', name: 'Test 1', status: 'passed', duration_ms: 100, started_at: '2026-01-01' },
      { id: '2', name: 'Test 2', status: 'failed', duration_ms: 200, started_at: '2026-01-01' },
      { id: '3', name: 'Test 3', status: 'failed', duration_ms: 300, started_at: '2026-01-01' },
    ];

    expect(store.totalRuns).toBe(3);
    expect(store.failedRuns).toBe(2); // Two tests have the 'failed' status
  });

  it('fetches mock runs and updates state', async () => {
    const store = useTestRunsStore();
    
    // Trigger the async action
    const fetchPromise = store.fetchMockRuns();
    
    // It should immediately be in a loading state
    expect(store.isLoading).toBe(true);
    
    // Wait for the mock API to "resolve"
    await fetchPromise;
    
    // Check the final state
    expect(store.isLoading).toBe(false);
    expect(store.runs.length).toBeGreaterThan(0);
    expect(store.error).toBeNull();
  });
});