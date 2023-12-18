from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import Any
from typing_extensions import Literal

from matplotlib.axes import Axes
from matplotlib.colors import Normalize
from matplotlib.typing import ColorType, LineStyleType, MarkerType

from ._core.typing import ColumnName, DataSource, Default
from .axisgrid import FacetGrid
from .external.kde import _BwMethodType
from .utils import _DataSourceWideForm, _ErrorBar, _Estimator, _Legend, _LogScale, _Palette, _Seed, _Vector

__all__ = ["catplot", "stripplot", "swarmplot", "boxplot", "violinplot", "boxenplot", "pointplot", "barplot", "countplot"]

def boxplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    dodge: bool | Literal["auto"] = "auto",
    width: float = 0.8,
    gap: float = 0,
    whis: float = 1.5,
    linecolor: ColorType = "auto",
    linewidth: float | None = None,
    fliersize: float | None = None,
    hue_norm: tuple[float, float] | Normalize | None = None,
    native_scale: bool = False,
    log_scale: _LogScale | None = None,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def violinplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    inner: str | None = "box",
    split: bool = False,
    width: float = 0.8,
    dodge: bool | Literal["auto"] = "auto",
    gap: float = 0,
    linewidth: float | None = None,
    linecolor: ColorType = "auto",
    cut: float = 2,
    gridsize: int = 100,
    bw_method: _BwMethodType = "scott",
    bw_adjust: float = 1,
    density_norm: Literal["area", "count", "width"] = "area",
    common_norm: bool | None = False,
    hue_norm: tuple[float, float] | Normalize | None = None,
    formatter: Callable[[Any], str] | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    legend: _Legend = "auto",
    scale: Incomplete = ...,  # deprecated
    scale_hue: Incomplete = ...,  # deprecated
    bw: Incomplete = ...,  # deprecated
    inner_kws: dict[str, Any] | None = None,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def boxenplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    dodge: bool | Literal["auto"] = "auto",
    width: float = 0.8,
    gap: float = 0,
    linewidth: float | None = None,
    linecolor: ColorType | None = None,
    width_method: Literal["exponential", "linear", "area"] = "exponential",
    k_depth: Literal["tukey", "proportion", "trustworthy", "full"] | int = "tukey",
    outlier_prop: float = 0.007,
    trust_alpha: float = 0.05,
    showfliers: bool = True,
    hue_norm: tuple[float, float] | Normalize | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    scale: Incomplete = ...,  # deprecated
    box_kws: dict[str, Any] | None = None,
    flier_kws: dict[str, Any] | None = None,
    line_kws: dict[str, Any] | None = None,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def stripplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    jitter: float | Literal[True] = True,
    dodge: bool = False,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    size: float = 5,
    edgecolor: ColorType | Default = ...,
    linewidth: float = 0,
    hue_norm: tuple[float, float] | Normalize | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def swarmplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    dodge: bool = False,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    size: float = 5,
    edgecolor: ColorType | None = None,
    linewidth: float = 0,
    hue_norm: tuple[float, float] | Normalize | None = None,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    warn_thresh: float = 0.05,
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def barplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    estimator: _Estimator = "mean",
    errorbar: _ErrorBar | None = ("ci", 95),
    n_boot: int = 1000,
    units: ColumnName | _Vector | None = None,
    seed: _Seed | None = None,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    hue_norm: tuple[float, float] | Normalize | None = None,
    width: float = 0.8,
    dodge: bool | Literal["auto"] = "auto",
    gap: float = 0,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    capsize: float = 0,
    err_kws: dict[str, Any] | None = None,
    ci: Incomplete = ...,  # deprecated
    errcolor: Incomplete = ...,  # deprecated
    errwidth: Incomplete = ...,  # deprecated
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def pointplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    estimator: _Estimator = "mean",
    errorbar: _ErrorBar | None = ("ci", 95),
    n_boot: int = 1000,
    units: ColumnName | _Vector | None = None,
    seed: _Seed | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    hue_norm: tuple[float, float] | Normalize | None = None,
    markers: MarkerType | list[MarkerType] | Default = ...,
    linestyles: LineStyleType | list[LineStyleType] | Default = ...,
    dodge: bool = False,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    orient: Literal["v", "h", "x", "y"] | None = None,
    capsize: float = 0,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    err_kws: dict[str, Any] | None = None,
    ci: Incomplete = ...,  # deprecated
    errwidth: Incomplete = ...,  # deprecated
    join: Incomplete = ...,  # deprecated
    scale: Incomplete = ...,  # deprecated
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def countplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    saturation: float = 0.75,
    fill: bool = True,
    hue_norm: tuple[float, float] | Normalize | None = None,
    stat: Literal["count", "percent", "proportion", "probability"] = "count",
    width: float = 0.8,
    dodge: bool | Literal["auto"] = "auto",
    gap: float = 0,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[[Any], str] | None = None,
    legend: _Legend = "auto",
    ax: Axes | None = None,
    **kwargs: Any,
) -> Axes: ...
def catplot(
    data: DataSource | _DataSourceWideForm | None = None,
    *,
    x: ColumnName | _Vector | None = None,
    y: ColumnName | _Vector | None = None,
    hue: ColumnName | _Vector | None = None,
    row: ColumnName | _Vector | None = None,
    col: ColumnName | _Vector | None = None,
    kind: Literal["strip", "swarm", "box", "violin", "boxen", "point", "bar", "count"] = "strip",
    estimator: _Estimator = "mean",
    errorbar: _ErrorBar | None = ("ci", 95),
    n_boot: int = 1000,
    units: ColumnName | _Vector | None = None,
    seed: _Seed | None = None,
    order: Iterable[ColumnName] | None = None,
    hue_order: Iterable[ColumnName] | None = None,
    row_order: Iterable[ColumnName] | None = None,
    col_order: Iterable[ColumnName] | None = None,
    col_wrap: int | None = None,
    height: float = 5,
    aspect: float = 1,
    log_scale: _LogScale | None = None,
    native_scale: bool = False,
    formatter: Callable[[Any], str] | None = None,
    orient: Literal["v", "h", "x", "y"] | None = None,
    color: ColorType | None = None,
    palette: _Palette | None = None,
    hue_norm: tuple[float, float] | Normalize | None = None,
    legend: _Legend = "auto",
    legend_out: bool = True,
    sharex: bool = True,
    sharey: bool = True,
    margin_titles: bool = False,
    facet_kws: dict[str, Any] | None = None,
    ci: Incomplete = ...,  # deprecated
    **kwargs: Any,
) -> FacetGrid: ...
