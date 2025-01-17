from edgar._companies import get_entity_submissions, Entity


def test_entity_is_company():
    # TSLA
    assert get_entity_submissions(1318605).is_company

    # Taneja Vaibhav at TSLA
    assert not get_entity_submissions(1771340).is_company

    # &VEST Domestic Fund II LP
    assert get_entity_submissions(1800903).is_company

    # Siemens AG
    assert get_entity_submissions(940418).is_company

    # SIEMENS ENERGY AG/ADR
    assert get_entity_submissions(1830056).is_company

    # SIEVERT STEPHANIE A
    assert not get_entity_submissions(1718179).is_company

    assert Entity(1911716).is_company

    # Warren Buffett
    assert not Entity(315090).is_company

    # NVC Holdings, LLC
    assert Entity(1940261).is_company

    # FANNIE MAE
    assert Entity(310522).is_company

    # Berkshire Hathaway
    assert Entity(1067983).is_company

    # ORBIMED Advisors LLC
    assert Entity(1055951).is_company


def test_display_name():
    assert Entity(1318605).display_name == "Tesla, Inc."

    assert Entity(1830610).name == 'Michaels Lisa Anne'
    assert Entity(1830610).display_name == "Lisa Anne Michaels"

    assert Entity(1718179).name == "Sievert Stephanie A"
    assert Entity(1718179).display_name == "Stephanie A Sievert"


def test_insider_transaction_for_entity():
    entity: Entity = Entity(1940261)
    assert entity.name == "NVC Holdings, LLC"
    assert not entity.insider_transaction_for_issuer_exists
    assert entity.insider_transaction_for_owner_exists

    entity = Entity(1599916)
    assert not entity.is_company
    assert not entity.insider_transaction_for_issuer_exists
    assert entity.insider_transaction_for_owner_exists
    assert entity.name == "DeNunzio Jeffrey"
