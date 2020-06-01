def test_malware_readable_data():
    from FireEyeETP import malware_readable_data
    try:
        malware_readable_data({'name': 'some-name'})
    except KeyError:
        assert False, 'malware_readable_data method should not fail on dict with name key only'
