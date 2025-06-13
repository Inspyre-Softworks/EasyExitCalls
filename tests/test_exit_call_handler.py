from easy_exit_calls import ExitCallHandler


def setup_function(_):
    """Clear handlers before each test."""
    ExitCallHandler().clear_handlers()


def teardown_function(_):
    """Clear handlers after each test."""
    ExitCallHandler().clear_handlers()


def test_lifo_execution_order():
    calls = []

    def first():
        calls.append("first")

    def second():
        calls.append("second")

    ech = ExitCallHandler()
    ech.register_handler(first)
    ech.register_handler(second)

    ech.call_handlers()

    assert calls == ["second", "first"]


def test_unregister_by_uuid():
    def handler():
        pass

    ech = ExitCallHandler()
    uid = ech.register_handler(handler)

    # Unregistering a valid UUID should succeed
    assert ech.find_handler_by_uuid(uid) is not None
    assert ech.unregister_by_uuid(uid) is True
    assert ech.find_handler_by_uuid(uid) is None

    # Unregistering the same UUID again should return False
    assert ech.unregister_by_uuid(uid) is False

    # Unregistering a random/non-existent UUID should return False
    import uuid
    random_uid = uuid.uuid4()
    assert ech.unregister_by_uuid(random_uid) is False


def test_unregister_all_with_name():
    def target(a=None):
        pass

    def other():
        pass

    ech = ExitCallHandler()
    ech.register_handler(target, 1)
    ech.register_handler(target, 2)
    ech.register_handler(other)

    ech.unregister_all_with_name("target")

    names = [h["handler_info"]["name"] for h in ech.handlers]
    assert names == ["other"]

