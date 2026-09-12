/**
 * sflabs (The Steadfast Labs) - Enterprise AI PoC Feasibility & ROI Engine + Lead Routing
 * 
 * Implements:
 * 1. Technical Feasibility Score (0-100%) based on data readiness, stack maturity, compliance and complexity
 * 2. Financial ROI & OPEX Savings projections (BRL)
 * 3. Break-even & Payback timeline calculation (Months)
 * 4. Risk Mitigation & Hallucination Containment Value
 * 5. Intelligent Lead Scoring & Automated Routing (Tier 1 Enterprise FDE, Tier 2 Technical PoC, Tier 3 Discovery)
 */

class LabsROIEngine {
  constructor() {
    this.benchmarks = {
      // Human analyst cost benchmark (BRL/month default)
      avgFteMonthlyCostBrl: 12000,
      // Hours per month
      workingHoursPerMonth: 168,
      // Baseline error cost multiplier
      avgCostPerReworkIncidentBrl: 450,
      // Labs 30-day Sandbox PoC reference cost (BRL)
      labsSandboxPocCostBrl: 85000,
      // Traditional Big 4 / Generalist IT consultancies estimated cost
      big4TraditionalCostBrl: 320000,
      // Standard AI automation efficiency gain range (60% - 85%)
      efficiencyFactor: 0.72,
      // Error reduction factor with SMT Guardrails & Deterministic FDE (80% - 95%)
      errorReductionFactor: 0.88
    };
  }

  /**
   * Calculate ROI, OPEX Savings, and Feasibility Score
   * @param {Object} params
   * @returns {Object} Calculated metrics
   */
  calculate(params) {
    const {
      monthlyVolume = 10000,           // Operations/queries/tickets per month
      timePerOpMinutes = 15,           // Minutes spent per manual operation
      fteCount = 5,                    // Number of human operators / analysts
      currentErrorRate = 25,           // % current error/rework rate
      complexityLevel = 'moderate',    // 'low' | 'moderate' | 'high' | 'mission_critical'
      vertical = 'bfsi',               // 'bfsi' | 'healthcare' | 'logistics' | 'retail' | 'other'
      dataReadiness = 'structured',    // 'structured' | 'hybrid' | 'unstructured_silos' | 'legacy_mess'
      governanceReq = 'high'           // 'standard' | 'high' | 'extreme_bacen_hipaa'
    } = params;

    // 1. Current Baseline Cost Calculations
    const monthlyTotalManualHours = (monthlyVolume * timePerOpMinutes) / 60;
    const requiredFteFromVolume = Math.max(fteCount, monthlyTotalManualHours / this.benchmarks.workingHoursPerMonth);
    const monthlyLaborCost = requiredFteFromVolume * this.benchmarks.avgFteMonthlyCostBrl;
    
    // Rework & Error financial impact
    const monthlyReworkIncidents = monthlyVolume * (currentErrorRate / 100);
    const monthlyErrorCost = monthlyReworkIncidents * this.benchmarks.avgCostPerReworkIncidentBrl;
    
    const monthlyTotalBaselineCost = monthlyLaborCost + monthlyErrorCost;
    const annualTotalBaselineCost = monthlyTotalBaselineCost * 12;

    // 2. Projected Labs FDE AI Deployment Impact
    const monthlySavedHours = monthlyTotalManualHours * this.benchmarks.efficiencyFactor;
    const monthlyLaborSavings = (monthlySavedHours / this.benchmarks.workingHoursPerMonth) * this.benchmarks.avgFteMonthlyCostBrl;
    const monthlyErrorSavings = monthlyErrorCost * this.benchmarks.errorReductionFactor;
    
    const monthlyTotalSavings = monthlyLaborSavings + monthlyErrorSavings;
    const annualTotalSavings = monthlyTotalSavings * 12;

    // 3. Investment & Payback
    let estimatedInvestment = this.benchmarks.labsSandboxPocCostBrl;
    if (complexityLevel === 'high') estimatedInvestment *= 1.35;
    if (complexityLevel === 'mission_critical') estimatedInvestment *= 1.8;
    if (governanceReq === 'extreme_bacen_hipaa') estimatedInvestment *= 1.25;

    const netAnnualBenefit = annualTotalSavings - estimatedInvestment;
    const roiPercentage = Math.round((netAnnualBenefit / estimatedInvestment) * 100);
    const paybackPeriodMonths = Math.max(0.5, Math.min(24, (estimatedInvestment / monthlyTotalSavings))).toFixed(1);

    // Traditional Big 4 comparison
    const traditionalCost = this.benchmarks.big4TraditionalCostBrl * (complexityLevel === 'mission_critical' ? 1.6 : 1.2);
    const upfrontSavingsVsBig4 = Math.max(0, traditionalCost - estimatedInvestment);

    // 4. Feasibility Score (0 - 100)
    let feasibilityScore = 70; // baseline

    // Adjust based on data readiness
    if (dataReadiness === 'structured') feasibilityScore += 18;
    else if (dataReadiness === 'hybrid') feasibilityScore += 8;
    else if (dataReadiness === 'unstructured_silos') feasibilityScore -= 10;
    else if (dataReadiness === 'legacy_mess') feasibilityScore -= 22;

    // Adjust based on complexity
    if (complexityLevel === 'low') feasibilityScore += 12;
    else if (complexityLevel === 'moderate') feasibilityScore += 5;
    else if (complexityLevel === 'high') feasibilityScore -= 5;
    else if (complexityLevel === 'mission_critical') feasibilityScore -= 12;

    // Adjust based on governance
    if (governanceReq === 'standard') feasibilityScore += 5;
    else if (governanceReq === 'high') feasibilityScore += 0;
    else if (governanceReq === 'extreme_bacen_hipaa') feasibilityScore -= 5;

    // Clamp score 15 to 98
    feasibilityScore = Math.max(20, Math.min(98, feasibilityScore));

    let feasibilityStatus = 'Alta Viabilidade';
    let feasibilityColor = '#10B981'; // green
    let feasibilitySummary = 'Caso de uso ideal para PoC em Sandbox de 30 dias com alto ROI e rápida implantação.';

    if (feasibilityScore < 50) {
      feasibilityStatus = 'Alta Complexidade / Requer Sanity Sprint';
      feasibilityColor = '#EF4444'; // red
      feasibilitySummary = 'Requer estruturação prévia de dados e arquitetura de guardrails antes do rollout amplo.';
    } else if (feasibilityScore < 75) {
      feasibilityStatus = 'Viabilidade Moderada';
      feasibilityColor = '#F59E0B'; // yellow/amber
      feasibilitySummary = 'Viável com arquitetura de Knowledge Graph / RAG avançado e validação contínua.';
    }

    return {
      monthlyVolume,
      annualTotalBaselineCost: Math.round(annualTotalBaselineCost),
      annualTotalSavings: Math.round(annualTotalSavings),
      monthlyTotalSavings: Math.round(monthlyTotalSavings),
      estimatedInvestment: Math.round(estimatedInvestment),
      netAnnualBenefit: Math.round(netAnnualBenefit),
      roiPercentage,
      paybackPeriodMonths: parseFloat(paybackPeriodMonths),
      traditionalCost: Math.round(traditionalCost),
      upfrontSavingsVsBig4: Math.round(upfrontSavingsVsBig4),
      feasibilityScore,
      feasibilityStatus,
      feasibilityColor,
      feasibilitySummary,
      savedHoursPerMonth: Math.round(monthlySavedHours),
      errorIncidentsAvoidedPerMonth: Math.round(monthlyReworkIncidents * this.benchmarks.errorReductionFactor)
    };
  }
}

/**
 * Lead Qualification and Automated Routing Engine
 */
class LabsLeadRouter {
  /**
   * Process qualification form inputs and assign routing tier
   * @param {Object} leadData
   * @param {Object} roiResult
   * @returns {Object} Lead profile with score, tier, destination and webhook payload
   */
  static processLead(leadData, roiResult = {}) {
    const {
      name = '',
      email = '',
      company = '',
      phone = '',
      role = '',
      vertical = 'bfsi',
      budgetRange = '150k_400k',
      timeline = 'immediate',
      techStack = [],
      primaryPain = 'hallucinations',
      projectScope = ''
    } = leadData;

    let leadScore = 0;
    const reasons = [];

    // 1. Role Scoring
    const roleLower = (role || '').toLowerCase();
    if (roleLower.includes('cto') || roleLower.includes('cio') || roleLower.includes('vp') || roleLower.includes('head') || roleLower.includes('director') || roleLower.includes('diretor') || roleLower.includes('c-level')) {
      leadScore += 30;
      reasons.push('Decisor Técnico / Executivo (+30)');
    } else if (roleLower.includes('lead') || roleLower.includes('manager') || roleLower.includes('gerente') || roleLower.includes('arquiteto') || roleLower.includes('architect')) {
      leadScore += 20;
      reasons.push('Influenciador Técnico (+20)');
    } else {
      leadScore += 10;
      reasons.push('Avaliador (+10)');
    }

    // 2. Budget Scoring
    if (budgetRange === '400k_1m_plus') {
      leadScore += 35;
      reasons.push('Orçamento Enterprise > R$ 400k (+35)');
    } else if (budgetRange === '150k_400k') {
      leadScore += 25;
      reasons.push('Orçamento FDE Piloto R$ 150k-400k (+25)');
    } else if (budgetRange === '50k_150k') {
      leadScore += 15;
      reasons.push('Orçamento PoC Sandbox R$ 50k-150k (+15)');
    } else {
      leadScore += 5;
      reasons.push('Orçamento em Definição (+5)');
    }

    // 3. Timeline Urgency
    if (timeline === 'immediate') {
      leadScore += 20;
      reasons.push('Início Imediato < 30 dias (+20)');
    } else if (timeline === '1_3_months') {
      leadScore += 12;
      reasons.push('Planejado para 1-3 meses (+12)');
    } else {
      leadScore += 5;
      reasons.push('Horizonte Exploratório (+5)');
    }

    // 4. Vertical Strategic Fit
    if (vertical === 'bfsi' || vertical === 'healthcare') {
      leadScore += 15;
      reasons.push('Vertical Estratégica Prioritária Labs (BFSI/Healthcare) (+15)');
    } else {
      leadScore += 8;
      reasons.push('Vertical Geral (+8)');
    }

    // 5. Corporate Domain Verification (Penalty for generic emails)
    const isPublicEmail = /@(gmail|hotmail|yahoo|outlook|live|icloud|bol|uol)\./i.test(email);
    if (isPublicEmail) {
      leadScore -= 10;
      reasons.push('Email não corporativo (-10)');
    } else if (email.includes('@')) {
      leadScore += 10;
      reasons.push('Domínio corporativo verificado (+10)');
    }

    leadScore = Math.max(10, Math.min(100, leadScore));

    // Determine Tier & Route
    let tier = 'TIER_3_DISCOVERY';
    let priorityLabel = 'P3 — Nutrição & Material Técnico';
    let assignedTeam = 'GTM & Business Development';
    let targetSla = 'Até 48 horas';
    let actionRecommendation = 'Disponibilizar whitepaper de Governança e agendar introdução comercial.';

    if (leadScore >= 75 || budgetRange === '400k_1m_plus' || (budgetRange === '150k_400k' && timeline === 'immediate')) {
      tier = 'TIER_1_ENTERPRISE_FDE';
      priorityLabel = 'P1 — Enterprise FDE Prioritário';
      assignedTeam = 'Head de Engenharia / Lead FDE Partner';
      targetSla = '< 4 horas úteis (Mesmo Dia)';
      actionRecommendation = 'Convite imediato para Briefing de Arquitetura & Demonstração de Sandbox.';
    } else if (leadScore >= 45 || budgetRange === '150k_400k' || budgetRange === '50k_150k') {
      tier = 'TIER_2_TECHNICAL_POC';
      priorityLabel = 'P2 — Technical PoC Sandbox';
      assignedTeam = 'FDE Solutions Architect';
      targetSla = '< 24 horas';
      actionRecommendation = 'Envio de questionário de maturidade de dados e proposta de PoC de 30 dias.';
    }

    // Build Webhook & CRM Payload
    const timestamp = new Date().toISOString();
    const webhookPayload = {
      event: 'lead_qualified',
      timestamp,
      tier,
      lead_score: leadScore,
      priority_label: priorityLabel,
      contact: {
        name,
        email,
        phone,
        company,
        role
      },
      project_profile: {
        vertical,
        budget_range: budgetRange,
        timeline,
        tech_stack: techStack,
        primary_pain: primaryPain,
        scope_notes: projectScope
      },
      roi_projections: roiResult ? {
        feasibility_score: roiResult.feasibilityScore,
        feasibility_status: roiResult.feasibilityStatus,
        projected_annual_savings_brl: roiResult.annualTotalSavings,
        estimated_roi_pct: roiResult.roiPercentage,
        payback_months: roiResult.paybackPeriodMonths,
        estimated_investment_brl: roiResult.estimatedInvestment
      } : null,
      routing: {
        assigned_team: assignedTeam,
        sla_window: targetSla,
        next_action: actionRecommendation,
        scoring_factors: reasons
      }
    };

    return {
      tier,
      leadScore,
      priorityLabel,
      assignedTeam,
      targetSla,
      actionRecommendation,
      scoringReasons: reasons,
      webhookPayload
    };
  }
}

// Export for Node / Browser usage
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { LabsROIEngine, LabsLeadRouter };
}
