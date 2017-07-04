#!/usr/bin/env python

# Copyright 2017 The Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import miniflow as tf


def main():
  a = tf.placeholder(tf.float32)
  b = tf.constant(32.0)
  c = tf.add(a, b)

  sess = tf.Session()
  print(sess.run(c, feed_dict={a: 10}))
  print(sess.run(c, feed_dict={a.name: 10}))


if __name__ == "__main__":
  main()
