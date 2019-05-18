from fizzbuzz import fizzbuzz
import pytest

def test_fb_is_callable():
    fizzbuzz(1)

def test_fb_returns_str():
    assert isinstance(fizzbuzz(1), str) 

@pytest.mark.parametrize('num', [1, 2, 4])
def test_fb_regular_is_self(num):
    assert int(fizzbuzz(num)) == num
    

@pytest.mark.parametrize('num', [3, 6, 9])
def test_fb_regular_is_fizz(num):
    assert fizzbuzz(num) == 'fizz'


@pytest.mark.parametrize('num', [5, 20, 50])
def test_fb_regular_is_buzz(num):
    assert fizzbuzz(num) == 'buzz'


@pytest.mark.parametrize('num', [15, 30, 3000])
def test_fb_regular_is_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'

def test_fb_raises_typerror_on_str():
    with pytest.raises(TypeError):
        fizzbuzz("")


@pytest.mark.parametrize('num', [ "", 1.5, [], 4+3j])
def test_fb_regular_is_fizzbuzz(num):
      with pytest.raises(TypeError):
        fizzbuzz(num)

    

