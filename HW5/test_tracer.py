from tracer import fibbonacci_luca

def test_fibbonacci():
    assert fibbonacci_luca("fibbonacci", 0) == 0
    assert fibbonacci_luca("fibbonacci", 1) == 1
    assert fibbonacci_luca("fibbonacci", 2) == 1
    assert fibbonacci_luca("fibbonacci", 3) == 2
    assert fibbonacci_luca("fibbonacci", 4) == 3
    assert fibbonacci_luca("fibbonacci", 5) == 5

def test_luca():
    assert fibbonacci_luca("luca", 0) == 2
    assert fibbonacci_luca("luca", 1) == 1
    assert fibbonacci_luca("luca", 2) == 3
    assert fibbonacci_luca("luca", 3) == 4
    assert fibbonacci_luca("luca", 4) == 7

result_strings_1 = """Вызываем fibbonacci_luca с позиционными аргументами ('luca', 3) и именованными аргументами {}
  Вызываем fibbonacci_luca с позиционными аргументами ('luca', 2) и именованными аргументами {}
    Вызываем fibbonacci_luca с позиционными аргументами ('luca', 1) и именованными аргументами {}
    Возвращаем 1
    Вызываем fibbonacci_luca с позиционными аргументами ('luca', 0) и именованными аргументами {}
    Возвращаем 2
  Возвращаем 3
  Вызываем fibbonacci_luca с позиционными аргументами ('luca', 1) и именованными аргументами {}
  Возвращаем 1
Возвращаем 4
"""

result_strings_2="""Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci',) и именованными аргументами {'n': 4}
  Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 3) и именованными аргументами {}
    Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 2) и именованными аргументами {}
      Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 1) и именованными аргументами {}
      Возвращаем 1
      Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 0) и именованными аргументами {}
      Возвращаем 0
    Возвращаем 1
    Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 1) и именованными аргументами {}
    Возвращаем 1
  Возвращаем 2
  Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 2) и именованными аргументами {}
    Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 1) и именованными аргументами {}
    Возвращаем 1
    Вызываем fibbonacci_luca с позиционными аргументами ('fibbonacci', 0) и именованными аргументами {}
    Возвращаем 0
  Возвращаем 1
Возвращаем 3
"""
def test_tracer(capsys):
    fibbonacci_luca("luca", 3)
    captured = capsys.readouterr()
    assert captured.out == result_strings_1

    fibbonacci_luca("fibbonacci", n=4)
    captured = capsys.readouterr()
    assert captured.out == result_strings_2