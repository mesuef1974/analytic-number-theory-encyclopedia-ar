# Build the three named imakeidx indexes declared with noautomatic.
# Latexmk treats each dotted suffix as a custom dependency of main.tex.

add_cus_dep('people.idx', 'people.ind', 0, 'make_people_index');
add_cus_dep('theorems.idx', 'theorems.ind', 0, 'make_theorems_index');
add_cus_dep('symbols.idx', 'symbols.ind', 0, 'make_symbols_index');

sub make_people_index {
    my ($base) = @_;
    return system("makeindex -o \"$base.people.ind\" \"$base.people.idx\"");
}

sub make_theorems_index {
    my ($base) = @_;
    return system("makeindex -o \"$base.theorems.ind\" \"$base.theorems.idx\"");
}

sub make_symbols_index {
    my ($base) = @_;
    return system("makeindex -o \"$base.symbols.ind\" \"$base.symbols.idx\"");
}
