from playwright.sync_api import Page, expect

from pages.tasks_page import TasksPage
from test_data.tasks import VALID_TASK


def test_user_can_create_a_task(page: Page):
    tasks_page = TasksPage(page)

    # Arrange
    tasks_page.open()

    # Act
    tasks_page.create_task(
        name=VALID_TASK["name"],
        description=VALID_TASK["description"],
    )

    # Assert
    task = tasks_page.get_task(
        VALID_TASK["name"]
    )

    expect(task).to_be_visible()

    expect(
        task
    ).to_contain_text(
        VALID_TASK["description"]
    )

    expect(
        tasks_page.task_success
    ).to_be_visible()


def test_task_name_boundary_values(page: Page):
    tasks_page = TasksPage(page)

    # Arrange
    tasks_page.open()

    # 2 characters - invalid
    tasks_page.create_task(
        name="AB"
    )

    expect(
        tasks_page.task_error
    ).to_be_visible()

    # 3 characters - valid
    tasks_page.task_name.fill("ABC")
    tasks_page.add_task_button.click()

    expect(
        tasks_page.get_task("ABC")
    ).to_be_visible()

    # 100 characters - valid
    task_100_chars = "A" * 100

    tasks_page.task_name.fill(
        task_100_chars
    )

    tasks_page.add_task_button.click()

    expect(
        tasks_page.get_task(task_100_chars)
    ).to_be_visible()

    # 101 characters - browser should enforce maxlength=100
    task_101_chars = "A" * 101

    tasks_page.task_name.fill(
        task_101_chars
    )

    expect(
        tasks_page.task_name
    ).to_have_value(
        "A" * 100
    )