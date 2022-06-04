"""Tests for verbum.verbum module."""
import pytest

from verbum import verbum


class TestParsing:
    """Test parsing of version string."""

    @staticmethod
    @pytest.mark.parametrize(
        "version_str", ["1.1.1.1", "12.1.1.1", "1.12.1.1", "1.1.12.1", "1.1.1.12"]
    )
    def test_parsing_four_number_version(version_str: str) -> None:
        """Test 4 number versions are invalid."""
        with pytest.raises(ValueError, match=f"Unparsable version: {version_str}"):
            verbum.Version(version_str)

    @staticmethod
    @pytest.mark.parametrize("version_str", ["1.1.1", "12.1.1", "1.12.1", "1.1.12"])
    def test_parsing_three_number_version(version_str: str) -> None:
        """Test 3 number versions are valid."""
        verbum.Version(version_str)  # act

    @staticmethod
    @pytest.mark.parametrize("version_str", ["1.1", "12.1", "1.12"])
    def test_parsing_two_number_version(version_str: str) -> None:
        """Test 2 number versions are invalid."""
        with pytest.raises(ValueError, match=f"Unparsable version: {version_str}"):
            verbum.Version(version_str)

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [
            f"{v}{pre}"
            for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]
            for pre in [
                "-a1",
                ".a1",
                "_a1",
                "alpha1",
                "-b1",
                ".b1",
                "_b1",
                "beta1",
                "-rc1",
                ".rc1",
                "_rc1",
                "c1",
            ]
        ],
    )
    def test_parsing_invalid_pre_release(version_str: str) -> None:
        """Test invalid pre-releases."""
        with pytest.raises(ValueError, match=f"Unparsable version: {version_str}"):
            verbum.Version(version_str)

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [
            f"{v}{pre}"
            for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]
            for pre in ["a1", "b1", "rc1"]
        ],
    )
    def test_parsing_valid_pre_release(version_str: str) -> None:
        """Test valid pre-releases."""
        verbum.Version(version_str)  # act

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [
            f"{v}{pre}"
            for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]
            for pre in ["post1", "-post1", "_post1"]
        ],
    )
    def test_parsing_invalid_post_release(version_str: str) -> None:
        """Test invalid post-releases."""
        with pytest.raises(ValueError, match=f"Unparsable version: {version_str}"):
            verbum.Version(version_str)

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [f"{v}.post1" for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]],
    )
    def test_parsing_valid_post_release(version_str: str) -> None:
        """Test valid post-releases."""
        verbum.Version(version_str)  # act

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [
            f"{v}{pre}"
            for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]
            for pre in ["dev1", "-dev1", "_dev1"]
        ],
    )
    def test_parsing_invalid_dev_release(version_str: str) -> None:
        """Test invalid dev-releases."""
        with pytest.raises(ValueError, match=f"Unparsable version: {version_str}"):
            verbum.Version(version_str)

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [f"{v}.dev1" for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]],
    )
    def test_parsing_valid_dev_release(version_str: str) -> None:
        """Test valid dev-releases."""
        verbum.Version(version_str)  # act

    @staticmethod
    @pytest.mark.parametrize(
        "version_str",
        [
            f"{v}{pre}"
            for v in ["1.1.1", "12.1.1", "1.12.1", "1.1.12"]
            for pre in ["a0", "b0", "rc0", ".post0", ".dev0"]
        ],
    )
    def test_parsing_identifier_with_0(version_str: str) -> None:
        """Test identifier with 0 are invalid."""
        with pytest.raises(ValueError, match=r"0 is not a valid [a-z]{2,5} counter"):
            verbum.Version(version_str)
