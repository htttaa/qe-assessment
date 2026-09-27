from playwright.sync_api import Page, expect

from pages.tasks_page import TasksPage
from test_data.tasks import VALID_TASK, VALID_SUBTASK


def test_user_can_create_a_subtask(page: Page):
    tasks_page = TasksPage(page)

    # Arrange
    tasks_page.open()

    tasks_page.create_task(
        name=VALID_TASK["name"],
        description=VALID_TASK["description"],
    )

    # Act
    tasks_page.open_subtask_modal(
        VALID_TASK["name"]
    )

    # Assert - modal is visible
    expect(
        tasks_page.subtask_modal
    ).to_be_visible()

    # Assert - task information is displayed
    expect(
        tasks_page.subtask_task_id
    ).to_be_visible()

    expect(
        tasks_page.subtask_task_description
    ).to_have_value(
        VALID_TASK["description"]
    )

    # Act - create subtask
    tasks_page.create_subtask(
        description=VALID_SUBTASK["description"],
        due_date=VALID_SUBTASK["due_date"],
    )

    # Assert - success message
    expect(
        tasks_page.subtask_success
    ).to_be_visible()

    # Assert - subtask was added
    expect(
        tasks_page.subtask_list
    ).to_contain_text(
        VALID_SUBTASK["description"]
    )

    # Assert - subtask counter was updated
    expect(
        tasks_page.subtask_count
    ).to_have_text("1")