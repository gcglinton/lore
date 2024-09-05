"""Make schema

Revision ID: f8b8f06308a7
Revises: 
Create Date: 2024-09-03 11:14:03.097072

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "f8b8f06308a7"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cloud_providers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name_short", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("contact_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("contact_email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("contact_phone", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_cloud_providers_is_deleted"),
        "cloud_providers",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "departments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("acronym", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "environment_code",
            sqlmodel.sql.sqltypes.AutoString(length=2),
            nullable=False,
        ),
        sa.Column("cio_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("cio_email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("cloud_dg_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("cloud_dg_email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("aom_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("aom_email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("client_exec_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("client_exec_email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("sdm_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("sdm_email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_science", sa.Boolean(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_departments_is_deleted"), "departments", ["is_deleted"], unique=False)
    op.create_index(op.f("ix_departments_is_science"), "departments", ["is_science"], unique=False)
    op.create_table(
        "experiment_areaofscience",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiment_areaofscience_is_deleted"),
        "experiment_areaofscience",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "experiment_datasensitivity",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiment_datasensitivity_is_deleted"),
        "experiment_datasensitivity",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "experiment_fundingsource",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name_short", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiment_fundingsource_is_deleted"),
        "experiment_fundingsource",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "experiment_levelofeffort",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiment_levelofeffort_is_deleted"),
        "experiment_levelofeffort",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "experiment_statuses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiment_statuses_is_deleted"),
        "experiment_statuses",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "experiment_tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiment_tags_is_deleted"),
        "experiment_tags",
        ["is_deleted"],
        unique=False,
    )
    op.create_table(
        "users_roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_roles_is_deleted"), "users_roles", ["is_deleted"], unique=False)
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name_first", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name_last", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("phone", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("department", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("notes", sa.TEXT(), nullable=True),
        sa.Column("is_legoteam", sa.Boolean(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["department"],
            ["departments.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_is_deleted"), "users", ["is_deleted"], unique=False)
    op.create_index(op.f("ix_users_is_legoteam"), "users", ["is_legoteam"], unique=False)
    op.create_table(
        "experiments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("status", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("created_user", sa.Integer(), nullable=True),
        sa.Column("delegated", sa.Boolean(), nullable=True),
        sa.Column("department", sa.Integer(), nullable=False),
        sa.Column("research_initiative", sa.Integer(), nullable=True),
        sa.Column("area_of_science", sa.Integer(), nullable=True),
        sa.Column("level_of_effort", sa.Integer(), nullable=True),
        sa.Column("funding_source", sa.Integer(), nullable=True),
        sa.Column("data_sensivitity", sa.Integer(), nullable=True),
        sa.Column("cloud_provider_requested", sa.Integer(), nullable=True),
        sa.Column("cloud_provider_actual", sa.Integer(), nullable=True),
        sa.Column("background", sa.TEXT(), nullable=True),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.Column("goals", sa.TEXT(), nullable=True),
        sa.Column("fin_forecasted", sa.Float(), nullable=True),
        sa.Column("fin_initial", sa.Float(), nullable=True),
        sa.Column("fin_actual", sa.Float(), nullable=True),
        sa.Column("fin_automated_reports", sa.Boolean(), nullable=True),
        sa.Column("progress", sa.Integer(), nullable=True),
        sa.Column("environment_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("is_deleted", sa.Boolean(), nullable=True),
        sa.Column("is_archived", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["area_of_science"],
            ["experiment_areaofscience.id"],
        ),
        sa.ForeignKeyConstraint(
            ["cloud_provider_actual"],
            ["cloud_providers.id"],
        ),
        sa.ForeignKeyConstraint(
            ["cloud_provider_requested"],
            ["cloud_providers.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_user"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["data_sensivitity"],
            ["experiment_datasensitivity.id"],
        ),
        sa.ForeignKeyConstraint(
            ["department"],
            ["departments.id"],
        ),
        sa.ForeignKeyConstraint(
            ["funding_source"],
            ["experiment_fundingsource.id"],
        ),
        sa.ForeignKeyConstraint(
            ["level_of_effort"],
            ["experiment_levelofeffort.id"],
        ),
        sa.ForeignKeyConstraint(
            ["status"],
            ["experiment_statuses.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_experiments_fin_automated_reports"),
        "experiments",
        ["fin_automated_reports"],
        unique=False,
    )
    op.create_index(
        op.f("ix_experiments_is_archived"), "experiments", ["is_archived"], unique=False
    )
    op.create_index(op.f("ix_experiments_is_deleted"), "experiments", ["is_deleted"], unique=False)
    op.create_index(op.f("ix_experiments_status"), "experiments", ["status"], unique=False)
    op.create_table(
        "link_experiments_related",
        sa.Column("experiment_1", sa.Integer(), nullable=False),
        sa.Column("experiment_2", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["experiment_1"],
            ["experiments.id"],
        ),
        sa.ForeignKeyConstraint(
            ["experiment_2"],
            ["experiments.id"],
        ),
        sa.PrimaryKeyConstraint("experiment_1", "experiment_2"),
    )
    op.create_table(
        "link_experiments_tags",
        sa.Column("experiment_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["experiment_id"],
            ["experiments.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["experiment_tags.id"],
        ),
        sa.PrimaryKeyConstraint("experiment_id", "tag_id"),
    )
    op.create_table(
        "link_experiments_users",
        sa.Column("experiment_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["experiment_id"],
            ["experiments.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["users_roles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("experiment_id", "user_id", "role_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("link_experiments_users")
    op.drop_table("link_experiments_tags")
    op.drop_table("link_experiments_related")
    op.drop_index(op.f("ix_experiments_status"), table_name="experiments")
    op.drop_index(op.f("ix_experiments_is_deleted"), table_name="experiments")
    op.drop_index(op.f("ix_experiments_is_archived"), table_name="experiments")
    op.drop_index(op.f("ix_experiments_fin_automated_reports"), table_name="experiments")
    op.drop_table("experiments")
    op.drop_index(op.f("ix_users_is_legoteam"), table_name="users")
    op.drop_index(op.f("ix_users_is_deleted"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_users_roles_is_deleted"), table_name="users_roles")
    op.drop_table("users_roles")
    op.drop_index(op.f("ix_experiment_tags_is_deleted"), table_name="experiment_tags")
    op.drop_table("experiment_tags")
    op.drop_index(op.f("ix_experiment_statuses_is_deleted"), table_name="experiment_statuses")
    op.drop_table("experiment_statuses")
    op.drop_index(
        op.f("ix_experiment_levelofeffort_is_deleted"),
        table_name="experiment_levelofeffort",
    )
    op.drop_table("experiment_levelofeffort")
    op.drop_index(
        op.f("ix_experiment_fundingsource_is_deleted"),
        table_name="experiment_fundingsource",
    )
    op.drop_table("experiment_fundingsource")
    op.drop_index(
        op.f("ix_experiment_datasensitivity_is_deleted"),
        table_name="experiment_datasensitivity",
    )
    op.drop_table("experiment_datasensitivity")
    op.drop_index(
        op.f("ix_experiment_areaofscience_is_deleted"),
        table_name="experiment_areaofscience",
    )
    op.drop_table("experiment_areaofscience")
    op.drop_index(op.f("ix_departments_is_science"), table_name="departments")
    op.drop_index(op.f("ix_departments_is_deleted"), table_name="departments")
    op.drop_table("departments")
    op.drop_index(op.f("ix_cloud_providers_is_deleted"), table_name="cloud_providers")
    op.drop_table("cloud_providers")
    # ### end Alembic commands ###
