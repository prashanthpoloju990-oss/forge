/**
 * FORGE Type-Safe API Client
 * Connects the React UI to the FastAPI backend endpoints.
 */

const API_BASE = '/api';

export interface CommandResponse {
  status: string;
  agent_matched: string;
  intent: string;
  confidence: number;
  title: string;
  summary: string;
  metadata: { label: string; value: string }[];
  action_prepared?: {
    action_type: string;
    payload: any;
    primary_button: string;
    secondary_button: string;
  };
}

export interface MonteCarloResponse {
  status: string;
  iterations: number;
  input_parameters: {
    starting_cash: number;
    base_monthly_burn: number;
    headcount_added: number;
    additional_monthly_burn: number;
    capital_inflow: number;
  };
  summary: {
    median_runway_months: number;
    conservative_p10_months: number;
    optimistic_p90_months: number;
    prob_exhaustion_before_12mo: string;
    prob_exhaustion_before_18mo: string;
    health_assessment: string;
  };
  trajectories: {
    labels: string[];
    p10_conservative: number[];
    p50_median: number[];
    p90_optimistic: number[];
  };
}

export const forgeApi = {
  // Health & Heartbeat
  async checkHealth() {
    try {
      const res = await fetch(`${API_BASE}/health`);
      if (!res.ok) throw new Error('Health check failed');
      return await res.json();
    } catch (err) {
      console.warn('Backend offline, running in local in-memory mode');
      return null;
    }
  },

  // ⌘K Natural Language Command Parser
  async sendCommand(query: string, startupName?: string): Promise<CommandResponse | null> {
    try {
      const res = await fetch(`${API_BASE}/command`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, startup_name: startupName || 'Acme Inc.' }),
      });
      if (!res.ok) throw new Error('Command execution failed');
      return await res.json();
    } catch (err) {
      console.warn('API call failed, falling back to local orchestrator', err);
      return null;
    }
  },

  // Apply Command Action
  async executeCommandAction(actionType: string, payload: any) {
    try {
      const res = await fetch(`${API_BASE}/command/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action_type: actionType, payload }),
      });
      return await res.json();
    } catch (err) {
      console.warn('Action execution failed', err);
      return null;
    }
  },

  // Monte Carlo Runway Simulator
  async simulateTreasury(params: {
    starting_cash?: number;
    base_monthly_burn?: number;
    headcount_added?: number;
    capital_inflow?: number;
  }): Promise<MonteCarloResponse | null> {
    try {
      const res = await fetch(`${API_BASE}/finance/simulate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params),
      });
      if (!res.ok) throw new Error('Simulation failed');
      return await res.json();
    } catch (err) {
      console.warn('Simulation failed', err);
      return null;
    }
  },

  // Delaware Legal Contract Synthesizer
  async generateLegalDoc(docType: string, counterparty: string, parameters?: any) {
    try {
      const res = await fetch(`${API_BASE}/legal/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          doc_type: docType,
          counterparty,
          parameters,
        }),
      });
      return await res.json();
    } catch (err) {
      console.warn('Legal synthesis failed', err);
      return null;
    }
  },

  // Investor Board Memo Generator
  async getInvestorMemo() {
    try {
      const res = await fetch(`${API_BASE}/investor/memo`);
      return await res.json();
    } catch (err) {
      console.warn('Investor memo generation failed', err);
      return null;
    }
  },
};
