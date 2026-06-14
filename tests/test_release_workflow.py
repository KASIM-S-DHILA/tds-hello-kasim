from pathlib import Path


def test_release_smoke_test_import_uses_real_package_name():
    workflow = Path(".github/workflows/release.yml").read_text(encoding="utf-8")

    assert "tds_hello_YOURNAME" not in workflow
    assert "from tds_hello_kasim import greet" in workflow
