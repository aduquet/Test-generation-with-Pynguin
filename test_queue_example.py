# Automatically generated by Pynguin.
import pytest
import queue_example as module_0
import collections as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "%B?zT?q(/){)F\n5r72"
    module_0.place_order(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    deque_0 = module_1.deque()
    queue_0 = module_0.Queue()
    none_type_0 = module_0.place_order(queue_0, deque_0)
    queue_1 = module_0.Queue()
    none_type_0.exec_module(deque_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "d!.<E"
    queue_0 = module_0.Queue()
    bool_0 = queue_0.is_empty()
    assert bool_0 is True
    none_type_0 = queue_0.enqueue(str_0)
    queue_1 = module_0.Queue()
    bool_1 = queue_1.is_empty()
    assert bool_1 is True
    none_type_1 = module_0.serve_order(queue_0)
    assert len(queue_0.buffer) == 0
    assert none_type_1 is None
    none_type_0.is_empty()


def test_case_3():
    queue_0 = module_0.Queue()


def test_case_4():
    none_type_0 = None
    queue_0 = module_0.Queue()
    none_type_1 = queue_0.enqueue(none_type_0)
    queue_1 = module_0.Queue()
    bool_0 = queue_1.is_empty()
    assert bool_0 is True
    int_0 = queue_1.size()


@pytest.mark.xfail(strict=True)
def test_case_5():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    queue_1 = module_0.Queue()
    queue_1.dequeue()


@pytest.mark.xfail(strict=True)
def test_case_6():
    queue_0 = module_0.Queue()
    int_0 = queue_0.size()
    queue_1 = module_0.Queue()
    bool_0 = queue_1.is_empty()
    assert bool_0 is True
    bool_0.create_module(queue_1)


def test_case_7():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.is_empty()
    assert bool_0 is True


@pytest.mark.xfail(strict=True)
def test_case_8():
    queue_0 = module_0.Queue()
    str_0 = module_0.serve_order(queue_0)
    assert str_0 == "Order queue is empty"
    queue_1 = module_0.Queue()
    bool_0 = queue_1.is_empty()
    assert bool_0 is True
    bool_0.create_module(queue_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    bool_0 = queue_0.is_empty()
    assert bool_0 is False
    queue_1 = module_0.Queue()
    none_type_1 = queue_0.enqueue(queue_0)
    none_type_2 = module_0.serve_order(queue_0)
    assert len(queue_0.buffer) == 0
    assert none_type_2 is None
    int_0 = queue_1.size()
    queue_2 = module_0.Queue()
    none_type_3 = queue_2.enqueue(none_type_0)
    int_1 = queue_0.size()
    assert int_1 == 0
    int_2 = queue_0.size()
    assert int_2 == 0
    int_2.is_empty()
