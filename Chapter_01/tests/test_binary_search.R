library(testthat)
source('../src/binary_search.R')

test_that('Empty arrays return FALSE', {
  array = c()

  expect_false(binary_search(array, 1))
})

test_that('Small arrays return expected checks', {
  array = seq(0, 9)

  expect_true(binary_search(array, 8))
  expect_false(binary_search(array, 11))
})

test_that('Arrays with negative values can be scanned', {
  array = seq(-10, 24)

  expect_true(binary_search(array, -4))
})

test_that('Large arrays return expected checks', {
  array = seq(0, 999999)

  expect_true(array, 823453)
  expect_false(array, 1000000)
})
