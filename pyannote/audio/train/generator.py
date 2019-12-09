#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)

# Copyright (c) 2019 CNRS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# AUTHORS
# Hervé BREDIN - http://herve.niderb.fr

"""
TODO
"""


from abc import ABCMeta, abstractmethod
from pyannote.audio.features.base import FeatureExtraction
from pyannote.database.protocol.protocol import Protocol
from typing import Optional, Iterator
try:
    from typing import Literal
except ImportError as e:
    from typing_extensions import Literal

# TODO: move this to pyannote.database
Subset = Optional[Literal['train', 'development', 'test']]

from torch.utils.data import IterableDataset


class SampleGenerator(IterableDataset,
                      metaclass=ABCMeta):
    """Sample generator base class

    Parameters
    ----------
    feature_extraction : `FeatureExtraction`
    protocol : `Protocol`
        pyannote.database protocol used by the generator.
    subset : {'train', 'development', 'test'}, optional
        Subset used by the generator. Defaults to 'train'.
    """

    @abstractmethod
    def __init__(self,
                 feature_extraction : FeatureExtraction,
                 protocol : Protocol,
                 subset : Subset = 'train',
                 **kwargs):
        pass

    @property
    @abstractmethod
    def specifications(self) -> dict:
        """Generator specifications

        Returns
        -------
        specifications : `dict`
            Dictionary describing generator specifications.
        """
        pass

    @property
    @abstractmethod
    def batches_per_epoch(self) -> int:
        """Number of batches per epoch

        Returns
        -------
        n_batches : `int`
            Number of batches to make an epoch.
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator:
        pass
