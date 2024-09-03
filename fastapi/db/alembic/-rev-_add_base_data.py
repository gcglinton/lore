"""Add base data

Revision ID: 9804c2247912
Revises: f8b8f06308a7
Create Date: 2024-09-03 11:16:24.357562

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "<ADD REV HERE>"
down_revision: Union[str, None] = "<ADD UPSTREAM REV HERE>"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    md = sqlmodel.SQLModel.metadata

    op.bulk_insert(
        md.tables["cloud_providers"],
        [
            {
                "id": 1,
                "name": "Amazon Web Services",
                "name_short": "AWS",
                "contact_name": "Daniel Maheux",
                "contact_email": "maheuxdr@amazon.com",
                "contact_phone": "4164362690",
            },
            {
                "id": 2,
                "name": "Google Cloud Platform",
                "name_short": "GCP",
                "contact_name": "Chris Carty",
                "contact_email": "chriscarty@google.com",
                "contact_phone": "",
            },
            {
                "id": 3,
                "name": "Microsoft Azure",
                "name_short": "AZ",
                "contact_name": "Graham McKendry",
                "contact_email": "gramck@microsoft.com",
                "contact_phone": "",
            },
        ],
    )

    op.bulk_insert(
        md.tables["departments"],
        [
            {
                "id": 1,
                "name": "Agriculture and Agri-Food",
                "acronym": "AAFC",
                "environment_code": "Aa",
                "is_science": True,
            },
            {
                "id": 2,
                "name": "Atlantic Canada Opportunities Agency",
                "acronym": "ACOA",
                "environment_code": "Ac",
                "is_science": False,
            },
            {
                "id": 3,
                "name": "Canada Border Services Agency",
                "acronym": "CBSA",
                "environment_code": "Cb",
                "is_science": False,
            },
            {
                "id": 4,
                "name": "Canadian Food Inspection Agency",
                "acronym": "CFIA",
                "environment_code": "Cf",
                "is_science": True,
            },
            {
                "id": 5,
                "name": "Canadian Heritage",
                "acronym": "CH",
                "environment_code": "Ch",
                "is_science": False,
            },
            {
                "id": 6,
                "name": "Canadian Nuclear Safety Commission",
                "acronym": "CNSC",
                "environment_code": "Ns",
                "is_science": True,
            },
            {
                "id": 7,
                "name": "Canadian Space Agency",
                "acronym": "CSA",
                "environment_code": "Sa",
                "is_science": True,
            },
            {
                "id": 8,
                "name": "Fisheries and Oceans Canada",
                "acronym": "DFO",
                "environment_code": "Fo",
                "is_science": True,
            },
            {
                "id": 9,
                "name": "National Defence",
                "acronym": "DND",
                "environment_code": "Nd",
                "is_science": False,
            },
            {
                "id": 10,
                "name": "Environment and Climate Change",
                "acronym": "ECCC",
                "environment_code": "Ec",
                "is_science": True,
            },
            {
                "id": 11,
                "name": "Health Canada",
                "acronym": "HC",
                "environment_code": "Hc",
                "is_science": True,
            },
            {
                "id": 12,
                "name": "Infrastructure Canada",
                "acronym": "IC",
                "environment_code": "Ic",
                "is_science": False,
            },
            {
                "id": 13,
                "name": "Indigenous Services Canada",
                "acronym": "ISC",
                "environment_code": "In",
                "is_science": False,
            },
            {
                "id": 14,
                "name": "Innovation, Science and Economic Development Canada",
                "acronym": "ISED",
                "environment_code": "Is",
                "is_science": False,
            },
            {
                "id": 15,
                "name": "National Research Council Canada",
                "acronym": "NRC",
                "environment_code": "Nr",
                "is_science": True,
            },
            {
                "id": 16,
                "name": "Natural Resources Canada",
                "acronym": "NRCan",
                "environment_code": "Na",
                "is_science": True,
            },
            {
                "id": 17,
                "name": "Parks Canada",
                "acronym": "PC",
                "environment_code": "Pc",
                "is_science": False,
            },
            {
                "id": 18,
                "name": "Public Health Agency of Canada",
                "acronym": "PHAC}",
                "environment_code": "Ph",
                "is_science": True,
            },
            {
                "id": 19,
                "name": "Polar Knowledge Canada",
                "acronym": "POLAR",
                "environment_code": "Pk",
                "is_science": False,
            },
            {
                "id": 20,
                "name": "Public Safety Canada",
                "acronym": "PSC",
                "environment_code": "Pa",
                "is_science": False,
            },
            {
                "id": 21,
                "name": "Public Services and Procurement Canada - Real Property",
                "acronym": "PSPC",
                "environment_code": "Pp",
                "is_science": False,
            },
            {
                "id": 22,
                "name": "Royal Canadian Mounted Police",
                "acronym": "RCMP",
                "environment_code": "Rc",
                "is_science": False,
            },
            {
                "id": 23,
                "name": "Shared Services Canada",
                "acronym": "SSC",
                "environment_code": "Sc",
                "is_science": False,
            },
            {
                "id": 24,
                "name": "Statistics Canada",
                "acronym": "StatCan",
                "environment_code": "St",
                "is_science": False,
            },
            {
                "id": 25,
                "name": "Transport Canada",
                "acronym": "TC",
                "environment_code": "Tc",
                "is_science": False,
            },
            {
                "id": 26,
                "name": "Transportation Safety Board",
                "acronym": "TSB",
                "environment_code": "Ts",
                "is_science": False,
            },
        ],
    )

    op.bulk_insert(
        md.tables["experiment_areaofscience"],
        [
            {"id": 1, "name": "Astronomy & Space Sciences"},
            {"id": 2, "name": "Computer Sciences"},
            {"id": 3, "name": "Data Sciences"},
            {"id": 4, "name": "Earth & Environmental Sciences"},
            {"id": 5, "name": "Life Sciences"},
            {"id": 6, "name": "Medical Sciences"},
            {"id": 7, "name": "Physical Sciences"},
        ],
    )

    op.bulk_insert(
        md.tables["experiment_datasensitivity"],
        [
            {"id": 1, "name": "Protected A"},
            {"id": 2, "name": "Protected B"},
            {"id": 3, "name": "Unclassified"},
        ],
    )

    # op.bulk_insert(
    #     md.tables["experiment_fundingsource"],
    #     [
    #         {
    #             "id": 1,
    #             "name": "Genomics Research and Development Initiative",
    #             "name_short": "GRDI",
    #         },
    #         {"id": 2, "name": "Labs Canada", "name_short": "Labs"},
    #         {"id": 3, "name": "Shared Services Canada", "name_short": "SSC"},
    #         {
    #             "id": 4,
    #             "name": "Shared Services Canada funds for ECCC",
    #             "name_short": "SSC-ECCC",
    #         },
    #         {
    #             "id": 5,
    #             "name": "Shared Services funds for Health Canada",
    #             "name_short": "SSC-HC",
    #         },
    #         {
    #             "id": 6,
    #             "name": "Shared Services Canada - High Performance Computing",
    #             "name_short": "SSC-HPC",
    #         },
    #         {
    #             "id": 7,
    #             "name": "Shared Services Canada funds for PHAC",
    #             "name_short": "SSC-PHAC",
    #         },
    #         {
    #             "id": 8,
    #             "name": "Shared Services Canada funds for Statistics Canada",
    #             "name_short": "SSC-STATS",
    #         },
    #     ],
    # )

    op.bulk_insert(
        md.tables["experiment_levelofeffort"],
        [
            {"id": 1, "name": "Space to play, no help required. (IaaS)"},
            {"id": 2, "name": "Some help, but mostly independant"},
            {"id": 3, "name": "Guidance required, best practices, setup. (PaaS)"},
            {"id": 4, "name": "Lots of help, but some independance"},
            {
                "id": 5,
                "name": "Full management, test software, get a VM, store data. (SaaS)",
            },
        ],
    )

    op.bulk_insert(
        md.tables["experiment_statuses"],
        [
            {"id": 1, "name": "Close Out"},
            {"id": 2, "name": "Complete"},
            {"id": 3, "name": "In Progress"},
            {"id": 4, "name": "New"},
            {"id": 5, "name": "Not Started"},
            {"id": 6, "name": "On Hold"},
            {"id": 7, "name": "Pending"},
            {"id": 8, "name": "Cancel"},
            {"id": 9, "name": "Queued"},
            {"id": 10, "name": "Rejected"},
            {"id": 11, "name": "Shared Resource"},
            {"id": 12, "name": "Approved"},
        ],
    )

    op.bulk_insert(
        md.tables["experiment_tags"],
        [
            {"id": 1, "name": "Containers"},
            {"id": 2, "name": "Data Sciences/Analytics"},
            {"id": 3, "name": "Artificial Intelligence"},
            {"id": 4, "name": "Machine Learning"},
            {"id": 5, "name": "Large Scale Computing"},
            {"id": 6, "name": "Quantum Computing"},
            {"id": 7, "name": "Software as a Service"},
        ],
    )

    op.bulk_insert(
        md.tables["users_roles"],
        [
            {"id": 1, "name": "Lego - Ops"},
            {"id": 2, "name": "Lego - EVO"},
            {"id": 3, "name": "Lego - Other"},
            {"id": 4, "name": "FinOps"},
            {"id": 5, "name": "Experiment Owner"},
            {"id": 6, "name": "Technical Owner"},
            {"id": 7, "name": "Technical Contributor"},
            {"id": 7, "name": "Technical Reader"},
            {"id": 8, "name": "Stakeholder"},
        ],
    )


def downgrade() -> None:
    md = sqlmodel.SQLModel.metadata

    op.execute(md.tables["departments"].delete())
    op.execute(md.tables["cloud_providers"].delete())
    op.execute(md.tables["experiment_areaofscience"].delete())
    op.execute(md.tables["experiment_datasensitivity"].delete())
    # op.execute(md.tables["experiment_fundingsource"].delete())
    op.execute(md.tables["experiment_levelofeffort"].delete())
    op.execute(md.tables["experiment_statuses"].delete())
    op.execute(md.tables["experiment_tags"].delete())
    op.execute(md.tables["users_roles"].delete())
