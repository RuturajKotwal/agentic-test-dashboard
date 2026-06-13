export type TestStatus = 'passed' | 'failed' | 'running' | 'pending';

export interface TestRun {
  id: string;
  name: string;
  status: TestStatus;
  duration_ms: number | null; // Null if still running/pending
  started_at: string; // ISO datetime string
}