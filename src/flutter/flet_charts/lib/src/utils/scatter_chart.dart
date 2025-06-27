import 'package:collection/collection.dart';
import 'package:equatable/equatable.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import 'charts.dart';

class ScatterChartEventData extends Equatable {
  final String eventType;
  final int? spotIndex;

  const ScatterChartEventData({required this.eventType, this.spotIndex});

  factory ScatterChartEventData.fromDetails(
      FlTouchEvent event, ScatterTouchResponse? response) {
    return ScatterChartEventData(
        eventType: eventMap[event.runtimeType.toString()] ?? "undefined",
        spotIndex: response?.touchedSpot?.spotIndex);
  }

  Map<String, dynamic> toMap() => {'type': eventType, 'spot_index': spotIndex};

  @override
  List<Object?> get props => [eventType, spotIndex];
}

ScatterTouchTooltipData? parseScatterTouchTooltipData(
    BuildContext context, Control control, List<ScatterSpot> spots,
    [ScatterTouchTooltipData? defaultValue]) {
  var tooltip = control.get("tooltip");
  if (tooltip == null) return defaultValue;

  final theme = Theme.of(context);

  return ScatterTouchTooltipData(
    tooltipBorder: parseBorderSide(tooltip["border_side"], theme,
        defaultValue: BorderSide.none)!,
    rotateAngle: parseDouble(tooltip["rotate_angle"]),
    maxContentWidth: parseDouble(tooltip["max_width"]),
    tooltipPadding: parsePadding(tooltip["padding"]),
    tooltipHorizontalAlignment: FLHorizontalAlignment.values
        .firstWhereOrNull((v) => v.name == tooltip["horizontal_alignment"]),
    tooltipHorizontalOffset: parseDouble(tooltip["horizontal_offset"]),
    tooltipBorderRadius: parseBorderRadius(tooltip["border_radius"]),
    fitInsideHorizontally: parseBool(tooltip["fit_inside_horizontally"]),
    fitInsideVertically: parseBool(tooltip["fit_inside_vertically"]),
    getTooltipColor: (ScatterSpot spot) {
      // var spotIndex =
      //     spots.indexWhere((spot) => spot.x == spot.x && spot.y == spot.y);
      // var dp = control.children("spots")[spotIndex];
      return parseColor(
          tooltip["bgcolor"], theme, const Color.fromRGBO(96, 125, 139, 1))!;
    },
    getTooltipItems: (touchedSpot) {
      var spotIndex = spots.indexWhere(
          (spot) => spot.x == touchedSpot.x && spot.y == touchedSpot.y);
      return parseScatterTooltipItem(
          control.children("spots")[spotIndex], touchedSpot, context);
    },
  );
}

ScatterTooltipItem? parseScatterTooltipItem(
    Control dataPoint, ScatterSpot spot, BuildContext context) {
  if (!dataPoint.getBool("show_tooltip", true)!) return null;

  final theme = Theme.of(context);

  var tooltip = dataPoint.get("tooltip");
  var style = parseTextStyle(tooltip["text_style"], theme, const TextStyle())!;
  if (style.color == null) {
    style = style.copyWith(color: spot.dotPainter.mainColor);
  }
  return ScatterTooltipItem(
      tooltip["text"] ?? dataPoint.getDouble("y").toString(),
      textStyle: style,
      textAlign: parseTextAlign(tooltip["text_align"], TextAlign.center)!,
      children: tooltip["text_spans"] != null
          ? parseTextSpans(tooltip["text_spans"], theme, (s, eventName,
              [eventData]) {
              s.triggerEvent(eventName, eventData);
            })
          : null);
}
