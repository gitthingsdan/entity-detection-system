from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Species(Base):
    __tablename__ = "species"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    generation: Mapped[str] = mapped_column(String(20))
    capture_rate: Mapped[int]
    growth_rate: Mapped[str] = mapped_column(String(20))
    egg_group_1: Mapped[str] = mapped_column(String(20))
    egg_group_2: Mapped[str | None] = mapped_column(String(20))
    is_legendary: Mapped[bool]
    is_mythical: Mapped[bool]
    url: Mapped[str] = mapped_column(String(100), unique=True)
    evolves_from_species_id: Mapped[int | None] = mapped_column(ForeignKey("species.id"))

    evolves_from_species: Mapped[Species | None] = relationship(remote_side=[id])
    pokemon: Mapped[list[Pokemon]] = relationship(back_populates="species")


class Pokemon(Base):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    type_1: Mapped[str] = mapped_column(String(10))
    type_2: Mapped[str | None] = mapped_column(String(10))
    order: Mapped[int]
    height: Mapped[int]
    weight: Mapped[int]
    base_experience: Mapped[int]
    ability_1: Mapped[str] = mapped_column(String(20))
    ability_2: Mapped[str | None] = mapped_column(String(20))
    ability_3: Mapped[str | None] = mapped_column(String(20))
    url: Mapped[str] = mapped_column(String(100), unique=True)
    species_id: Mapped[int] = mapped_column(ForeignKey("species.id"))

    species: Mapped[Species] = relationship(back_populates="pokemon")
    stats: Mapped[Stats] = relationship(back_populates="pokemon")


class Stats(Base):
    __tablename__ = "stats"

    id: Mapped[int] = mapped_column(primary_key=True)
    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"), unique=True)
    hp: Mapped[int]
    attack: Mapped[int]
    defense: Mapped[int]
    special_attack: Mapped[int]
    special_defense: Mapped[int]
    speed: Mapped[int]

    pokemon: Mapped[Pokemon] = relationship(back_populates="stats")
