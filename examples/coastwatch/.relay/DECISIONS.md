# Decisions

## D-001 — Raw observations are immutable

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** human-report
- **Verification:** verified
- **Evidence ref:** synthetic lab data policy `POL-DATA-02`
- **Checked at:** 2026-08-30T10:00:00Z
- **Accepted by/at:** Dr. Rivera / 2026-06-12T15:00:00Z
- **Supersedes / superseded by:** none
- **Decision:** Raw sensor exports in R-003 are never edited in place. Corrections
  produce a versioned derived asset with lineage.
- **Why:** Retains traceability from each reported value to an immutable observation.

## D-002 — Use calibration registry v2

- **Kind:** decision
- **Authority:** superseded
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** synthetic Git tag `pilot-2026-05`
- **Checked at:** 2026-08-30T10:05:00Z
- **Accepted by/at:** Dr. Rivera / 2026-05-04T12:00:00Z
- **Supersedes / superseded by:** superseded by D-004
- **Decision:** Pilot outputs used calibration registry v2.
- **Why:** Retained only to interpret legacy R-012; it does not govern v3.

## D-003 — Exclude sensor S-14 from v3

- **Kind:** decision
- **Authority:** provisional
- **Provenance:** inference
- **Verification:** unverified
- **Evidence ref:** R-005 anomaly panel, section `S-14 drift`
- **Checked at:** 2026-09-01T08:55:00Z
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
- **Checked at:** 2026-08-30T10:10:00Z
- **Accepted by/at:** Dr. Rivera / 2026-08-18T09:30:00Z
- **Supersedes / superseded by:** supersedes D-002
- **Decision:** All current salinity normalization uses calibration registry v3.
- **Why:** v3 incorporates the reference-probe recertification completed on
  2026-08-16.

