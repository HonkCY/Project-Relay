# Decisions

Migration provenance IDs resolve in [AUDIT](migration/AUDIT.md), with sanitized
captures in the [evidence registry](evidence/README.md).

## D-001 — Raw observations are immutable

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** synthetic lab data policy `POL-DATA-02`; EV-POLICY-01
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:32:00Z
- **Migration provenance:**
  [MC-009](migration/AUDIT.md#mc-009--raw-observations-remain-immutable-under-the-accepted-data-policy)
- **Accepted by/at:** Dr. Rivera / 2026-06-12T15:00:00Z
- **Supersedes / superseded by:** none
- **Decision:** Raw source records in R-003 and R-014 are never edited in place.
  Corrections produce a versioned derived asset with lineage.
- **Why:** Retains traceability from each reported value to an immutable observation.

## D-002 — Use calibration registry v2

- **Kind:** decision
- **Authority:** superseded
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** synthetic Git tag `pilot-2026-05`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-08-30T10:05:00Z
- **Migration provenance:**
  [CF-001](migration/AUDIT.md#cf-001--remembered-v2-path-conflicts-with-current-v3-configuration)
- **Accepted by/at:** Dr. Rivera / 2026-05-04T12:00:00Z
- **Supersedes / superseded by:** superseded by D-004
- **Decision:** Pilot outputs used calibration registry v2.
- **Why:** Retained only to interpret legacy R-012; it does not govern v3.

## D-003 — Exclude sensor S-14 from v3

- **Kind:** decision
- **Authority:** provisional
- **Provenance:** inference
- **Verification:** unverified
- **Evidence ref:** R-005 anomaly panel `S-14 drift`, R-013 tolerance, R-014 maintenance log
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T08:55:00Z
- **Migration provenance:**
  [MC-007](migration/AUDIT.md#mc-007--s-14-exclusion-remains-a-proposal-pending-pi-disposition)
- **Accepted by/at:** pending
- **Supersedes / superseded by:** none
- **Decision:** Exclude S-14 after 2026-08-17 from the v3 aggregate.
- **Why:** Reference-probe divergence exceeds the preregistered tolerance; the PI
  must still decide whether maintenance evidence justifies exclusion.

## D-004 — Use calibration registry v3

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** synthetic `config/calibration.yml` at commit `a1b2c3d`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-08-30T10:10:00Z
- **Migration provenance:**
  [MC-006](migration/AUDIT.md#mc-006--v3-is-the-current-normalization-output-family)
- **Accepted by/at:** Dr. Rivera / 2026-08-18T09:30:00Z
- **Supersedes / superseded by:** supersedes D-002
- **Decision:** All current salinity normalization uses calibration registry v3.
- **Why:** v3 incorporates the reference-probe recertification completed on
  2026-08-16.
